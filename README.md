# ProofRun Broken Demo

**Intentionally broken. Synthetic data. Not for production.**

A small storefront with many independent bugs for testing repository scans,
regression diagnosis, suggested fixes, and draft PR workflows. The bugs are the
point: do not weaken the tests to make the suite green.

## Run the tests

Requires Python 3.12.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

The baseline deliberately fails. GitHub Actions runs the same suite, so a red
build on the default branch is expected.

## Bug inventory

| Area | Deliberate issues |
| --- | --- |
| Pydantic | Eight nullable fields lack explicit defaults, breaking omission under v2 |
| pandas | Three calls use removed uppercase hourly aliases |
| Pricing | Discount arithmetic, cart quantities, tax-rate units, refund quantities |
| Fulfillment | Shipping threshold, inventory direction, cancellation status |
| Input handling | Email case normalization, negative quantities |
| Reporting | Pagination offset, empty average, reversed low-stock filter |
| Browser metrics | Legacy web-vitals exports, including FID migration requiring review |

There are 25 Python tests: 23 expose intentional defects and two passing controls
check that explicit null remains valid and object-valued nicknames remain invalid.
The JavaScript migration example is separate and has no browser test here.

## Try in ProofRun

Paste this repository's GitHub URL into **Public repository → Check repository**.
The scanner can flag the eight Pydantic fields, three pandas calls, and the
web-vitals import. It does not detect the twelve business-logic defects merely
by scanning. Execute the test suite to expose those.

Supported Pydantic/pandas findings can offer **Create draft PR**. Static proposals
remain unverified until tests execute. Fixing one issue should leave the other
intentional failures visible; passing a narrow test is not a clean full suite.

All records are fictional. No credentials, external services, databases, payments,
or production integrations are required to run the Python tests.
