# Vendor Risk Scoring Rubric

Defines how questionnaire responses convert to scores, how domain scores roll up, and how residual risk is calculated.

## Scoring Scale (per question)

| Response | Score | Criteria |
|----------|-------|----------|
| Yes / Fully implemented | 100% of question value | Control is documented, implemented, and evidence was provided (policy, report, or cert) |
| Partial | 50–60% of question value | Control exists but is undocumented, untested, or not enforced everywhere |
| No / Not implemented | 0 | Control absent, or vendor declined to answer |
| N/A (justified) | Excluded | Question removed from denominator only if justification is accepted by assessor |

Evidence beats attestation: a "Yes" without supporting evidence for Tier 1/2 vendors is scored as Partial.

## Domain Weights

| Domain | Weight | Rationale |
|--------|--------|-----------|
| Data Security & Encryption | 25% | Direct exposure of our data |
| Access Control & IAM | 20% | Most common breach vector for third parties |
| Incident Response & BCP | 20% | Determines blast radius and recovery when controls fail |
| Compliance & Certifications | 15% | Independent assurance (SOC 2, ISO 27001) |
| Network & Infrastructure Security | 10% | Perimeter and segmentation posture |
| Physical Security | 10% | Data center and device handling controls |

**Weighted score** = Σ (domain score % × domain weight), normalized to 100.

## Risk Tier Thresholds

| Weighted Score | Inherent Risk Rating | Disposition |
|----------------|---------------------|-------------|
| 85–100 | Low | Approve |
| 70–84 | Medium | Conditional approval + remediation plan |
| 50–69 | High | Conditional approval + 90-day remediation with re-test |
| < 50 | Critical | Reject, or exception per exception-management workflow |

## Inherent vs. Residual Risk

1. **Inherent risk** — the weighted questionnaire score, adjusted for data sensitivity and access level:
   - Vendor processes regulated data (PII/PHI/PCI): risk tier raised one level if score < 85
   - Vendor has privileged/network access to our environment: raised one level if score < 85
2. **Residual risk** — inherent risk after compensating controls we apply on our side (e.g., data minimization, network segmentation, contractual right-to-audit). Documented per assessment with a one-line justification for any downgrade.
3. Residual risk drives the final disposition and the re-assessment cadence (Low: annual; Medium: annual + quarterly attestation; High: semi-annual).
