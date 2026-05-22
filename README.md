# Third-Party Risk Management (TPRM) & Vendor Compliance Framework

**Enterprise-grade TPRM program using ISO 27001 Annex A and NIST CSF as evaluation baselines. Includes tiered vendor questionnaires, risk scoring rubrics, exception management workflows, and SOC 2 Type II assurance review templates.**

![ISO 27001](https://img.shields.io/badge/ISO_27001-Annex_A-0D47A1?style=flat)
![NIST CSF](https://img.shields.io/badge/NIST_CSF-Aligned-1565C0?style=flat)
![SOC 2](https://img.shields.io/badge/SOC_2-Type_II-003087?style=flat)

## Framework Overview

```
Vendor Onboarding
       │
       ▼
Tier Classification (Critical / High / Medium / Low)
       │
       ├──▶ Tier 1 (Critical) — Full questionnaire + on-site audit
       ├──▶ Tier 2 (High)     — Standard questionnaire + SOC 2 review
       ├──▶ Tier 3 (Medium)   — Lite questionnaire + cert verification
       └──▶ Tier 4 (Low)      — Self-attestation only
               │
               ▼
       Risk Scoring & Residual Risk Calculation
               │
               ▼
       Approve / Conditional / Reject + Exception Management
               │
               ▼
       Annual Re-Assessment + Continuous Monitoring
```

## Vendor Risk Scoring Model

| Domain | Weight | Max Score |
|--------|--------|-----------|
| Data Security & Encryption | 25% | 25 |
| Access Control & IAM | 20% | 20 |
| Incident Response & BCP | 20% | 20 |
| Compliance & Certifications | 15% | 15 |
| Network & Infrastructure Security | 10% | 10 |
| Physical Security | 10% | 10 |
| **Total** | **100%** | **100** |

**Risk Tier Thresholds:**
- Score 85–100: Low Risk → Approve
- Score 70–84: Medium Risk → Conditional Approval with remediation plan
- Score 50–69: High Risk → Conditional Approval with 90-day remediation
- Score < 50: Critical Risk → Reject / Exception required

## Repo Contents

```
tprm-vendor-risk-framework/
├── questionnaires/
│   ├── tier1-critical-vendor.md      # Full security questionnaire (80 questions)
│   ├── tier2-high-vendor.md          # Standard questionnaire (40 questions)
│   └── tier3-medium-vendor.md        # Lite questionnaire (20 questions)
├── risk-scoring/
│   └── vendor-risk-rubric.md         # Scoring criteria per domain
├── exception-management/
│   └── exception-workflow.md         # Exception request and approval process
├── templates/
│   └── vendor-risk-report.md         # Executive risk dashboard template
└── README.md
```

## Sample Vendor Assessment — Tier 2

| Question | Response | Score |
|----------|----------|-------|
| Do you hold SOC 2 Type II certification? | Yes (2024) | 15/15 |
| Is MFA enforced for all privileged access? | Yes | 10/10 |
| What is your RTO for critical systems? | 4 hours | 8/10 |
| Do you encrypt data at rest (AES-256)? | Yes | 10/10 |
| Is an incident response plan documented and tested? | Partially | 6/10 |
| **Total** | | **49/55** |

## References

- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [ISO 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [SOC 2 Trust Service Criteria](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [Shared Assessments SIG Questionnaire](https://sharedassessments.org/sig/)
