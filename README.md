# Third-Party Risk Management (TPRM) & Vendor Compliance Framework

**Enterprise-grade TPRM program using ISO 27001 Annex A and NIST CSF as evaluation baselines. Includes tiered vendor questionnaires, a weighted risk scoring rubric, exception management workflows, an executive reporting template, and a fully worked sample assessment.**

![ISO 27001](https://img.shields.io/badge/ISO_27001-Annex_A-0D47A1?style=flat)
![NIST CSF](https://img.shields.io/badge/NIST_CSF-Aligned-1565C0?style=flat)
![SOC 2](https://img.shields.io/badge/SOC_2-Type_II-003087?style=flat)

## Framework Overview

```
Vendor Onboarding
       |
       v
Tier Classification (Critical / High / Medium / Low)
       |
       +--> Tier 1 (Critical) -- Full questionnaire (65 q) + live audit
       +--> Tier 2 (High)     -- Standard questionnaire (40 q) + SOC 2 review
       +--> Tier 3 (Medium)   -- Lite questionnaire (19 q) + cert verification
       +--> Tier 4 (Low)      -- Self-attestation only
               |
               v
       Weighted Risk Scoring & Residual Risk Calculation
               |
               v
       Approve / Conditional / Reject + Exception Management
               |
               v
       Annual Re-Assessment + Continuous Monitoring
```

## Vendor Risk Scoring Model

| Domain | Weight |
|--------|--------|
| Data Security & Encryption | 25% |
| Access Control & IAM | 20% |
| Incident Response & BCP | 20% |
| Compliance & Certifications | 15% |
| Network & Infrastructure Security | 10% |
| Physical Security | 10% |

**Risk tier thresholds:** 85-100 Low (approve) | 70-84 Medium (conditional) | 50-69 High (conditional + 90-day remediation) | <50 Critical (reject / exception). Full scoring criteria, evidence rules, and inherent-vs-residual methodology in [`risk-scoring/vendor-risk-rubric.md`](risk-scoring/vendor-risk-rubric.md).

## Repo Contents

```
tprm-vendor-risk-framework/
|-- questionnaires/
|   |-- tier1-critical-vendor.md              # Full questionnaire, 65 questions, 6 domains
|   |-- tier2-high-vendor.md                  # Standard questionnaire, 40 questions
|   |-- tier3-medium-vendor.md                # Lite questionnaire, 19 questions
|   `-- sample-assessment-acme-cloud-tier2.md # Completed worked example with findings & disposition
|-- risk-scoring/
|   `-- vendor-risk-rubric.md                 # Scoring scale, weights, thresholds, residual risk
|-- exception-management/
|   `-- exception-workflow.md                 # Time-boxed risk acceptance process + record schema
|-- templates/
|   `-- vendor-risk-report.md                 # Executive assessment report template
|-- tprm-visuals/                             # Framework diagrams
`-- README.md
```

## Worked Example

See [`questionnaires/sample-assessment-acme-cloud-tier2.md`](questionnaires/sample-assessment-acme-cloud-tier2.md): a complete Tier 2 assessment of a fictional SaaS vendor — weighted score 81.3/100, Medium inherent risk, residual risk reduced via compensating controls, conditional approval with a tracked remediation plan.

## References

- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [ISO 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [SOC 2 Trust Service Criteria](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [Shared Assessments SIG Questionnaire](https://sharedassessments.org/sig/)
