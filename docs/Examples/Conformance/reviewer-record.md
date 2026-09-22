# Reviewer Record: Library Lending Export

**Implementation reviewed:** OCOM reference export, library lending example

**Reviewed against:** the model, Representation Map and Conformance Statement beside this file, at the commit that carries it

**Reviewer's relation to the claimant:** first party. The reviewer is the example's own author, so every judgment below is self-validation, which `Conformance-Test-Suite.md` Section 4 says the suite does not distinguish from independent validation and the publisher does. This record exists to show the format; it decides three Statements and leaves the rest pending on purpose.

A row is one named judgment on one Test the suite could not decide mechanically: a Review Test, or a mechanical Test the export could not settle. A judgment never overrides a mechanical Pass or Fail. Every cell is required; `tools/conformance/validate.py --reviews` refuses a record with an unknown Test, an outcome other than Review Pass or Review Fail, an unnamed reviewer, an unreadable date, an empty reason, or two rows for one Test.

| Test | Outcome | Reviewer | Date | Reason |
|---|---|---|---|---|
| REQ-MODELS-ENTITY-003 | Review Pass | Example reviewer (first party) | 22 September 2026 | The identifiers P-10432, LIB-000198 and LOAN-2026-08-0431 are accession and membership numbers the library assigns, carried as strings; nothing in the export ties them to a database key or a technology. |
| REQ-META-IDENTITY-001 | Review Pass | Example reviewer (first party) | 22 September 2026 | The export carries one snapshot, so stability over time cannot be observed in it; the identifiers are the ones the library has printed on cards and spines since the records were created, which is the evidence a reviewer has. |
| REQ-META-OWNERSHIP-001 | Review Pass | Example reviewer (first party) | 22 September 2026 | Each Ownership record names its owner, its owned object and a responsibility scope in plain words; ownership is explicit and traceable in the file, and nothing in it depends on a technology. |
