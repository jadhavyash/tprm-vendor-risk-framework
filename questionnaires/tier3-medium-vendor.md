# Tier 3 Vendor Security Questionnaire — Medium Risk

**Vendor Name:** _______________  
**Assessment Date:** _______________  
**Assessor:** _______________

Applies to vendors with limited access to internal or non-sensitive data. Lite questionnaire; certification verification in lieu of evidence collection; self-attestation accepted with annual re-confirmation.

## Section 1 — Data Security (30% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 1.1 | Is all data at rest encrypted using AES-256 or equivalent? | | | | /20 |
| 1.2 | Is all data in transit encrypted using TLS 1.2+? | | | | /20 |
| 1.3 | Are encryption keys managed in an HSM or managed KMS? | | | | /20 |
| 1.4 | Is key rotation performed at least annually? | | | | /20 |
| 1.5 | Is a data classification policy documented and enforced? | | | | /20 |

**Domain score: ___ / 100**

## Section 2 — Access Control (25% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 2.1 | Is MFA enforced for all remote access? | | | | /20 |
| 2.2 | Is MFA enforced for all privileged access? | | | | /20 |
| 2.3 | Is a PAM solution in use for administrative accounts? | | | | /20 |
| 2.4 | Is least-privilege enforced and reviewed at least quarterly? | | | | /20 |
| 2.5 | Are joiner/mover/leaver processes automated or ticketed with SLA? | | | | /20 |

**Domain score: ___ / 100**

## Section 3 — Incident Response (25% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 3.1 | Is a documented IR plan in place and reviewed annually? | | | | /25 |
| 3.2 | Is there a defined customer breach notification process within 72 hours? | | | | /25 |
| 3.3 | Do you carry cyber liability insurance? (state coverage) | | | | /25 |
| 3.4 | Is a BCP documented and tested annually? | | | | /25 |

**Domain score: ___ / 100**

## Section 4 — Compliance (20% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 4.1 | Do you hold a current SOC 2 Type II report? (provide) | | | | /20 |
| 4.2 | Do you hold ISO 27001 certification? (provide statement of applicability) | | | | /20 |
| 4.3 | Are penetration tests performed at least annually by a third party? | | | | /20 |
| 4.4 | Is there a dedicated security/compliance function with executive ownership? | | | | /20 |
| 4.5 | Is security awareness training completed annually by all staff? | | | | /20 |

**Domain score: ___ / 100**

## Scoring

Domain scores are weighted per `risk-scoring/vendor-risk-rubric.md` and rolled up to a weighted total /100.

**Weighted total: ___ / 100** — Inherent risk: ______ — Residual risk: ______
