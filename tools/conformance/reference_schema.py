#!/usr/bin/env python3
"""Derive the JSON Schema of the Reference Serialization from the example export, and check files against it.

`docs/Examples/Conformance/model.json` is the one encoding `CAND-026` publishes as the Reference
Serialization: not a format the specification prescribes, since `Language/Serialization.md`
prescribes none, but the one an implementation starts from when it has no encoding of its own. Its
schema is derived from the file and never written by hand, so the two cannot drift: --check
regenerates the schema and compares it with the committed one, then validates the model against it.

The schema validates a file in this encoding. It validates nothing about OCOM: what an export must
contain is decided by the Conformance Test Suite through the Representation Map, and a file that
satisfies this schema can still fail every Test in the catalogue.

  reference_schema.py --write            regenerate docs/Examples/Conformance/schema.json
  reference_schema.py --check            exit 1 if the committed schema differs from a regeneration
                                         or the model does not satisfy it
  reference_schema.py --validate FILE    check FILE against the committed schema; exit 1 on a violation
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODEL = ROOT / "docs" / "Examples" / "Conformance" / "model.json"
SCHEMA = ROOT / "docs" / "Examples" / "Conformance" / "schema.json"
DIGEST = "^[0-9a-f]{64}$"


def type_name(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    raise SystemExit("cannot derive a schema for a value of type %s" % type(value).__name__)


def type_schema(types):
    names = sorted(types)
    return {"type": names[0] if len(names) == 1 else names}


def column_schema(values):
    """The schema of one property, from every value it takes across the records."""
    types = {type_name(v) for v in values}
    out = type_schema(types)
    records = [v for v in values if isinstance(v, dict)]
    lists = [v for v in values if isinstance(v, list)]
    if records and types == {"object"} and all(records[0].keys() == r.keys() for r in records) and len(records) > 1:
        out.update(object_schema(records))
    if lists and all(isinstance(x, dict) for v in lists for x in v) and any(lists):
        out["items"] = object_schema([x for v in lists for x in v])
    elif lists and any(lists):
        out["items"] = type_schema({type_name(x) for v in lists for x in v})
    strings = [v for v in values if isinstance(v, str)]
    if strings and types == {"string"} and len(strings) > 1 and all(re.match(DIGEST, s) for s in strings):
        out["pattern"] = DIGEST
    return out


def object_schema(records):
    """An object schema over records of one kind: every property any record carries, required where
    all of them carry it and there are at least two records to compare (one record cannot tell an
    optional property from a mandatory one), additional properties allowed since an implementation
    extends the encoding before it replaces it."""
    keys = sorted({k for r in records for k in r})
    props = {k: column_schema([r[k] for r in records if k in r]) for k in keys}
    out = {"type": "object", "properties": props, "additionalProperties": True}
    if len(records) > 1:
        out["required"] = [k for k in keys if all(k in r for r in records)]
    return out


def derive(model):
    if not isinstance(model, dict):
        raise SystemExit("the model is not a JSON object; a schema over nothing cannot be checked")
    collections = {k: v for k, v in model.items() if isinstance(v, list) and v and all(isinstance(x, dict) for x in v)}
    if not collections:
        raise SystemExit("the model carries no collection of records; a schema over nothing cannot be checked")
    props = {}
    for key, value in model.items():
        if key in collections:
            props[key] = {"type": "array", "items": object_schema(value)}
        elif isinstance(value, dict):
            props[key] = object_schema([value])
        else:
            props[key] = column_schema([value])
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://ocom.uno/adoption/reference-serialization/schema.json",
        "title": "OCOM Reference Serialization",
        "description": ("Derived from docs/Examples/Conformance/model.json by tools/conformance/reference_schema.py and "
                        "never edited by hand (CAND-026). Validates a file in this encoding; it validates nothing about "
                        "OCOM, whose requirements the Conformance Test Suite reads through the Representation Map. "
                        "Collections are optional, an export carries the ones it has; a record's properties are "
                        "required only where every example record of its kind carries them and there are at least two "
                        "to compare. The specification prescribes no serialization format (Language/Serialization.md)."),
        "type": "object",
        "properties": props,
        # an export carries the collections it has and its map says which; only the block that
        # names who produced the file is required of every export
        "required": ["export"] if "export" in model else [],
        "additionalProperties": True,
    }


def render(model):
    return json.dumps(derive(model), indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def is_type(value, name):
    return {
        "null": value is None,
        "boolean": isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "string": isinstance(value, str),
        "array": isinstance(value, list),
        "object": isinstance(value, dict),
    }.get(name, False)


def violations(value, schema, path="$"):
    """Every way `value` fails `schema`, for the subset of JSON Schema this tool writes: type,
    properties, required, items, pattern."""
    types = schema.get("type")
    if types:
        names = types if isinstance(types, list) else [types]
        if not any(is_type(value, n) for n in names):
            yield "%s: expected %s, found %s" % (path, " or ".join(names), type_name(value))
            return
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                yield "%s: required key %s is missing" % (path, key)
        for key, sub in schema.get("properties", {}).items():
            if key in value:
                yield from violations(value[key], sub, "%s.%s" % (path, key))
    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            yield from violations(item, schema["items"], "%s[%d]" % (path, i))
    if isinstance(value, str) and "pattern" in schema and not re.match(schema["pattern"], value):
        yield "%s: %r does not match %s" % (path, value[:40], schema["pattern"])


def validate(path, schema_path=SCHEMA):
    if not schema_path.exists():
        raise SystemExit("%s does not exist; run --write" % schema_path)
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    found = list(violations(data, schema))
    for v in found[:20]:
        print("FAIL %s: %s" % (path, v))
    return found


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    g.add_argument("--validate", metavar="FILE")
    a = p.parse_args(argv)

    if a.validate:
        found = validate(a.validate)
        if found:
            return 1
        print("%s satisfies %s (a shape, not conformance: run the suite for that)" % (a.validate, SCHEMA.relative_to(ROOT)))
        return 0

    model = json.loads(MODEL.read_text(encoding="utf-8"))
    text = render(model)
    if a.write:
        SCHEMA.write_text(text, encoding="utf-8")
        print("wrote %s" % SCHEMA)
        return 0
    if not SCHEMA.exists():
        print("FAIL %s does not exist; run --write" % SCHEMA)
        return 1
    if SCHEMA.read_text(encoding="utf-8") != text:
        print("FAIL the committed schema differs from a regeneration; run --write")
        return 1
    if validate(MODEL):
        return 1
    print("schema up to date: %d collections, and the model satisfies it" % len([k for k, v in model.items() if isinstance(v, list)]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
