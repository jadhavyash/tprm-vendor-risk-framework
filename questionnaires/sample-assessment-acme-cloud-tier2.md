# Completed Sample Assessment — Acme Cloud Services (Tier 2)

**Vendor:** Acme Cloud Services (fictional — demonstration assessment)
**Service:** SaaS document collaboration platform holding internal business documents
**Data sensitivity:** Confidential (no regulated PII/PHI/PCI) · **Access:** No privileged access to our environment
**Assessment date:** 2026-06-15 · **Assessor:** Y. Jadhav · **Type:** Onboarding

## Domain Scores

| Domain | Weight | Findings Summary | Domain Score | Weighted |
|--------|--------|------------------|--------------|----------|
| Data Security & Encryption | 25% | AES-256 at rest, TLS 1.3 in transit, evidence provided. No DLP on egress (partial). Retention documented; disposal certificates provided. | 84 | 21.0 |
| Access Control & IAM | 20% | MFA on all remote + privileged access. PAM in use. Access reviews semi-annual, not quarterly (partial). Shared accounts vaulted. | 79 | 15.8 |
| Incident Response & BCP | 20% | IR plan tested 2026-02 (tabletop). RTO 6h (partial vs 4h target). 72h breach notification contractual. Cyber insurance $5M. | 81 | 16.2 |
| Compliance & Certifications | 15% | SOC 2 Type II current (report reviewed, 2 minor exceptions noted). No ISO 27001. Annual third-party pen test, summary shared. | 73 | 11.0 |
| Network & Infrastructure | 10% | Segmentation via VPC isolation. Monthly external scans. Criticals remediated ~20 days (partial vs 15-day target). EDR deployed. | 78 | 7.8 |
| Physical Security | 10% | Fully hosted on certified hyperscale cloud (inherits physical controls). | 95 | 9.5 |
| **Weighted total** | | | | **81.3 / 100** |

## Risk Determination

- **Inherent risk:** Medium (score 70–84 band). No sensitivity/access uplift applies — no regulated data, no privileged access.
- **Compensating controls (our side):** SSO enforced via our IdP; document uploads restricted by our own DLP policy; contract includes right-to-audit and 72h notification clause.
- **Residual risk: Medium → Low-Medium.** DLP gap on vendor side is materially offset by our egress DLP; access-review cadence gap is administrative.

## Key Findings & Remediation Plan

| # | Finding | Severity | Remediation | Due |
|---|---------|----------|-------------|-----|
| 1 | No vendor-side DLP on egress channels | Medium | Vendor roadmap commits DLP rollout Q4 2026; interim reliance on our egress DLP | 2026-12-31 |
| 2 | Access reviews semi-annual vs quarterly requirement | Low | Contractual commitment to quarterly reviews for our tenant | 2026-09-30 |
| 3 | Critical vuln remediation SLA ~20 days vs 15-day target | Low | Written commitment to 15-day SLA for internet-facing criticals | 2026-09-30 |
| 4 | SOC 2 report contained 2 minor exceptions (change mgmt evidence) | Low | Review auditor follow-up in next report cycle | Next SOC 2 cycle |

## Recommendation

**Conditional approval.** Engagement approved with remediation plan above tracked in the vendor risk register. Re-assessment cadence: annual, with remediation checkpoint at 2026-09-30. Escalate to exception workflow only if Finding 1 slips past Q4 2026.

**Approver:** Security Manager · **Date:** 2026-06-18
