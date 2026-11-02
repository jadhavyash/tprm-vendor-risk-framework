# Automated Vendor Risk Assessment Engine

A Python-based automation module that extends the existing Third-Party Risk Management (TPRM) framework.

## Overview

The engine calculates weighted vendor security scores, identifies missing mandatory controls, classifies preliminary risk levels, and generates structured JSON assessment reports.

## Features

- Automated weighted scoring across six security domains
- Vendor assessment input validation
- Risk classification: Low, Medium, High, Critical
- Mandatory security control validation
- Automated JSON report generation
- Unit tests for scoring and policy enforcement

## Architecture

1. `vendor_data/sample_vendor.json` — Sample vendor assessment input
2. `scoring.py` — Weighted scoring and risk classification
3. `policies.py` — Mandatory security control checks
4. `main.py` — Assessment execution and report generation
5. `reports/assessment.json` — Generated assessment output
6. `tests/test_scoring.py` — Automated unit tests

## Risk Scoring Weights

| Security Domain | Weight |
|---|---:|
| Data Security & Encryption | 25% |
| Access Control & IAM | 20% |
| Incident Response & BCP | 20% |
| Compliance & Certifications | 15% |
| Network & Infrastructure | 10% |
| Physical Security | 10% |

## Running the Application

From the root of the TPRM repository:

```bash
python -m automation.main
```

## Running Tests

```bash
python -m unittest discover -s automation/tests -v
```

## Security Design

The engine separates numerical risk scoring from mandatory security control validation.

A vendor with a high overall score can still require manual review when important security controls are missing.

The application generates recommendations only; it does not automatically authorize vendor onboarding.

## Current Limitations

This initial version accepts pre-calculated domain scores. It does not yet score individual questionnaire answers, verify supporting evidence, process justified N/A responses, or implement the complete inherent/residual-risk methodology.

The sample vendor is fictional and all input data is for demonstration purposes.

## Future Enhancements

- Questionnaire-level scoring
- Evidence validation workflow
- Tier-specific mandatory security requirements
- Risk adjustment and residual-risk assessment
- PDF and Markdown reporting
- Streamlit assessment dashboard
- Continuous monitoring and remediation tracking