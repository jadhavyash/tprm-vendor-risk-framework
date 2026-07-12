# Tier 1 Vendor Security Questionnaire — Critical

**Vendor Name:** _______________  
**Assessment Date:** _______________  
**Assessor:** _______________

Applies to vendors with privileged access, regulated data, or business-critical dependency. Full questionnaire; evidence required for all Yes answers; live audit session required.

## Section 1 — Data Security & Encryption (25% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 1.1 | Is all data at rest encrypted using AES-256 or equivalent? | | | | /8 |
| 1.2 | Is all data in transit encrypted using TLS 1.2+? | | | | /8 |
| 1.3 | Are encryption keys managed in an HSM or managed KMS? | | | | /8 |
| 1.4 | Is key rotation performed at least annually? | | | | /8 |
| 1.5 | Is a data classification policy documented and enforced? | | | | /8 |
| 1.6 | Is our data logically or physically segregated from other customers? | | | | /8 |
| 1.7 | Are data retention schedules documented and enforced? | | | | /8 |
| 1.8 | Is secure disposal (crypto-shred or certified destruction) performed and evidenced? | | | | /8 |
| 1.9 | Is DLP technology deployed on endpoints and egress channels? | | | | /8 |
| 1.10 | Are database activity monitoring controls in place? | | | | /8 |
| 1.11 | Is production data prohibited in non-production environments? | | | | /8 |
| 1.12 | Are backups encrypted and tested for restoration at least annually? | | | | /8 |
| 1.13 | Can you support our data deletion requests within contractual SLA? | | | | /8 |

**Domain score: ___ / 100**

## Section 2 — Access Control & IAM (20% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 2.1 | Is MFA enforced for all remote access? | | | | /8 |
| 2.2 | Is MFA enforced for all privileged access? | | | | /8 |
| 2.3 | Is a PAM solution in use for administrative accounts? | | | | /8 |
| 2.4 | Is least-privilege enforced and reviewed at least quarterly? | | | | /8 |
| 2.5 | Are joiner/mover/leaver processes automated or ticketed with SLA? | | | | /8 |
| 2.6 | Are access reviews for systems holding our data performed quarterly? | | | | /8 |
| 2.7 | Are shared/generic accounts prohibited or vaulted? | | | | /8 |
| 2.8 | Is SSO/federation supported for customer-facing access? | | | | /8 |
| 2.9 | Are service accounts inventoried with owners and rotation policy? | | | | /8 |
| 2.10 | Is session recording enabled for privileged access to systems holding our data? | | | | /8 |
| 2.11 | Are failed-login lockout and password policies aligned to NIST 800-63? | | | | /8 |
| 2.12 | Is customer data access restricted to named, background-checked staff? | | | | /8 |
| 2.13 | Is just-in-time access used for production environments? | | | | /8 |

**Domain score: ___ / 100**

## Section 3 — Incident Response & BCP (20% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 3.1 | Is a documented IR plan in place and reviewed annually? | | | | /8 |
| 3.2 | Has the IR plan been tested (tabletop or live) in the last 12 months? | | | | /8 |
| 3.3 | Is there a 24x7 security monitoring capability (internal or MDR)? | | | | /8 |
| 3.4 | What is your RTO for critical systems? (<4hr full, <8hr partial, >8hr zero) | | | | /8 |
| 3.5 | What is your RPO for systems holding our data? (<1hr full, <24hr partial) | | | | /8 |
| 3.6 | Is there a defined customer breach notification process within 72 hours? | | | | /8 |
| 3.7 | Do you carry cyber liability insurance? (state coverage) | | | | /8 |
| 3.8 | Is a BCP documented and tested annually? | | | | /8 |
| 3.9 | Are DR failover exercises performed at least annually? | | | | /8 |
| 3.10 | Is there a named incident commander / escalation chain? | | | | /8 |
| 3.11 | Do you commit to forensic cooperation and evidence preservation? | | | | /8 |
| 3.12 | Were any security incidents affecting customers reported in the last 24 months? (No=full; disclosed+remediated=partial) | | | | /8 |
| 3.13 | Are post-incident reviews documented with corrective actions? | | | | /8 |

**Domain score: ___ / 100**

## Section 4 — Compliance & Certifications (15% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 4.1 | Do you hold a current SOC 2 Type II report? (provide) | | | | /10 |
| 4.2 | Do you hold ISO 27001 certification? (provide statement of applicability) | | | | /10 |
| 4.3 | Are you PCI-DSS compliant (if handling cardholder data)? | | | | /10 |
| 4.4 | Are penetration tests performed at least annually by a third party? | | | | /10 |
| 4.5 | Are pen test executive summaries shareable under NDA? | | | | /10 |
| 4.6 | Is there a dedicated security/compliance function with executive ownership? | | | | /10 |
| 4.7 | Are subprocessors disclosed and flowed down equivalent obligations? | | | | /10 |
| 4.8 | Do you support customer right-to-audit contractually? | | | | /10 |
| 4.9 | Are privacy obligations (GDPR/CCPA as applicable) documented? | | | | /10 |
| 4.10 | Is security awareness training completed annually by all staff? | | | | /10 |

**Domain score: ___ / 100**

## Section 5 — Network & Infrastructure Security (10% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 5.1 | Is network segmentation in place between production, corporate, and customer environments? | | | | /10 |
| 5.2 | Are firewalls/security groups default-deny with documented rule review? | | | | /10 |
| 5.3 | Is vulnerability scanning performed at least monthly on internet-facing assets? | | | | /10 |
| 5.4 | Are critical vulnerabilities remediated within 15 days (high within 30)? | | | | /10 |
| 5.5 | Is EDR deployed on production servers and endpoints? | | | | /10 |
| 5.6 | Are IDS/IPS or equivalent detections in place at network boundaries? | | | | /10 |
| 5.7 | Is infrastructure defined as code with change control? | | | | /10 |
| 5.8 | Are cloud environments monitored with CSPM or equivalent? | | | | /10 |
| 5.9 | Is email security (SPF/DKIM/DMARC, phishing protection) enforced? | | | | /10 |
| 5.10 | Are administrative interfaces restricted to VPN/bastion access? | | | | /10 |

**Domain score: ___ / 100**

## Section 6 — Physical Security (10% weight)

| # | Question | Yes | No | Partial | Score |
|---|----------|-----|----|---------|-------|
| 6.1 | Are data centers certified (SOC 2 / ISO 27001) or in certified colo/cloud? | | | | /17 |
| 6.2 | Is badge or biometric access control enforced with visitor logging? | | | | /17 |
| 6.3 | Is CCTV coverage maintained for sensitive areas with retention policy? | | | | /17 |
| 6.4 | Are media and devices sanitized before disposal with certificates? | | | | /17 |
| 6.5 | Are clean-desk and device-encryption policies enforced for staff handling our data? | | | | /17 |
| 6.6 | Is physical access to systems holding our data reviewed at least annually? | | | | /17 |

**Domain score: ___ / 100**

## Scoring

Domain scores are weighted per `risk-scoring/vendor-risk-rubric.md` and rolled up to a weighted total /100.

**Weighted total: ___ / 100** — Inherent risk: ______ — Residual risk: ______
