# Exception Management Workflow

Governs cases where the business needs to engage a vendor that fails scoring thresholds, or an existing vendor falls below threshold at re-assessment.

## When an Exception Is Required

- Weighted score < 50 (Critical) and the business still requests engagement
- High-risk finding in a mandatory control (encryption at rest, MFA on privileged access, breach notification) regardless of total score
- Vendor unwilling to remediate within the 90-day window
- Expired certification (SOC 2 / ISO 27001) for a Tier 1 vendor

## Workflow

```
Business Owner submits Exception Request
        │  (business justification + duration requested)
        ▼
TPRM Analyst documents:
  - failed controls and score detail
  - risk statement (what could go wrong, likelihood, impact)
  - proposed compensating controls
        │
        ▼
Risk Review
  - Tier 3/4 vendor → Security Manager approval
  - Tier 2 vendor   → Security Manager + Business Unit head
  - Tier 1 vendor   → CISO (or delegate) + Business Unit head
        │
        ├── Rejected → engagement blocked; alternatives sourced
        ▼
Approved with conditions
  - compensating controls implemented and evidenced
  - exception entered in risk register with owner + expiry
        │
        ▼
Expiry / Re-review (max 12 months, 6 for Tier 1)
  - remediated → exception closed
  - not remediated → re-approval required at one level higher
```

## Exception Record — Required Fields

| Field | Description |
|-------|-------------|
| Exception ID | EX-YYYY-#### |
| Vendor / Tier | Name and classification |
| Failed control(s) | Question IDs + finding summary |
| Risk statement | Likelihood × impact, in business terms |
| Compensating controls | What reduces the risk in the interim |
| Approver(s) | Per tier routing above |
| Expiry date | Hard date; no evergreen exceptions |
| Owner | Accountable business owner, not TPRM |

## Principles

- Exceptions are time-boxed risk acceptances, not permanent waivers
- The business owns the risk; TPRM owns the record and the re-review
- Two consecutive renewals of the same exception triggers mandatory escalation one approval level up
