# Tier 2 Vendor Security Questionnaire — High Risk

**Vendor Name:** _______________  
**Assessment Date:** _______________  
**Assessor:** _______________

Applies to vendors handling sensitive data without privileged access. Standard questionnaire; current SOC 2 Type II (or ISO 27001) review required; evidence required for Data Security and Access Control sections.

## Section 1 — Data Security & Encryption (25% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 1.1 | Is all data at rest encrypted using AES-256 or equivalent? | | | | /12 |
| 1.2 | Is all data in transit encrypted using TLS 1.2+? | | | | /12 |
| 1.3 | Are encryption keys managed in an HSM or managed KMS? | | | | /12 |
| 1.4 | Is key rotation performed at least annually? | | | | /12 |
| 1.5 | Is a data classification policy documented and enforced? | | | | /12 |
| 1.6 | Is our data logically or physically segregated from other customers? | | | | /12 |
| 1.7 | Are data retention schedules documented and enforced? | | | | /12 |
| 1.8 | Is secure disposal (crypto-shred or certified destruction) performed and evidenced? | | | | /12 |

**Domain score: ___ / 100**

## Section 2 — Access Control & IAM (20% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 2.1 | Is MFA enforced for all remote access? | | | | /14 |
| 2.2 | Is MFA enforced for all privileged access? | | | | /14 |
| 2.3 | Is a PAM solution in use for administrative accounts? | | | | /14 |
| 2.4 | Is least-privilege enforced and reviewed at least quarterly? | | | | /14 |
| 2.5 | Are joiner/mover/leaver processes automated or ticketed with SLA? | | | | /14 |
| 2.6 | Are access reviews for systems holding our data performed quarterly? | | | | /14 |
| 2.7 | Are shared/generic accounts prohibited or vaulted? | | | | /14 |

**Domain score: ___ / 100**

## Section 3 — Incident Response & BCP (20% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 3.1 | Is a documented IR plan in place and reviewed annually? | | | | /12 |
| 3.2 | Has the IR plan been tested (tabletop or live) in the last 12 months? | | | | /12 |
| 3.3 | Is there a 24x7 security monitoring capability (internal or MDR)? | | | | /12 |
| 3.4 | What is your RTO for critical systems? (<4hr full, <8hr partial, >8hr zero) | | | | /12 |
| 3.5 | What is your RPO for systems holding our data? (<1hr full, <24hr partial) | | | | /12 |
| 3.6 | Is there a defined customer breach notification process within 72 hours? | | | | /12 |
| 3.7 | Do you carry cyber liability insurance? (state coverage) | | | | /12 |
| 3.8 | Is a BCP documented and tested annually? | | | | /12 |

**Domain score: ___ / 100**

## Section 4 — Compliance & Certifications (15% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 4.1 | Do you hold a current SOC 2 Type II report? (provide) | | | | /14 |
| 4.2 | Do you hold ISO 27001 certification? (provide statement of applicability) | | | | /14 |
| 4.3 | Are you PCI-DSS compliant (if handling cardholder data)? | | | | /14 |
| 4.4 | Are penetration tests performed at least annually by a third party? | | | | /14 |
| 4.5 | Are pen test executive summaries shareable under NDA? | | | | /14 |
| 4.6 | Is there a dedicated security/compliance function with executive ownership? | | | | /14 |
| 4.7 | Are subprocessors disclosed and flowed down equivalent obligations? | | | | /14 |

**Domain score: ___ / 100**

## Section 5 — Network & Infrastructure Security (10% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 5.1 | Is network segmentation in place between production, corporate, and customer environments? | | | | /17 |
| 5.2 | Are firewalls/security groups default-deny with documented rule review? | | | | /17 |
| 5.3 | Is vulnerability scanning performed at least monthly on internet-facing assets? | | | | /17 |
| 5.4 | Are critical vulnerabilities remediated within 15 days (high within 30)? | | | | /17 |
| 5.5 | Is EDR deployed on production servers and endpoints? | | | | /17 |
| 5.6 | Are IDS/IPS or equivalent detections in place at network boundaries? | | | | /17 |

**Domain score: ___ / 100**

## Section 6 — Physical Security (10% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 6.1 | Are data centers certified (SOC 2 / ISO 27001) or in certified colo/cloud? | | | | /25 |
| 6.2 | Is badge or biometric access control enforced with visitor logging? | | | | /25 |
| 6.3 | Is CCTV coverage maintained for sensitive areas with retention policy? | | | | /25 |
| 6.4 | Are media and devices sanitized before disposal with certificates? | | | | /25 |

**Domain score: ___ / 100**

## Scoring

Domain scores are weighted per `risk-scoring/vendor-risk-rubric.md` and rolled up to a weighted total /100.

**Weighted total: ___ / 100** — Inherent risk: ______ — Residual risk: ______
