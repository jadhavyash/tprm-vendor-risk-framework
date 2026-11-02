# 🛡️ Third-Party Risk Management (TPRM) & Automated Vendor Risk Assessment Framework

**A risk-based third-party security assessment framework with Python-powered risk scoring, security control validation, and automated assessment reporting.**

This project combines traditional Third-Party Risk Management (TPRM) methodologies with practical security engineering automation. It demonstrates how organizations can assess external vendors, evaluate security controls, quantify risk, identify security gaps, and generate consistent assessment recommendations.

The framework is aligned with **ISO 27001 Annex A** and **NIST Cybersecurity Framework (CSF) 2.0** principles, with SOC 2 evidence review incorporated into higher-risk vendor assessments.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![NIST CSF](https://img.shields.io/badge/NIST_CSF-2.0-1565C0)
![ISO 27001](https://img.shields.io/badge/ISO_27001-Annex_A-0D47A1)
![SOC 2](https://img.shields.io/badge/SOC_2-Evidence_Review-003087)
![Security Automation](https://img.shields.io/badge/Security-Automation-success)

---

## 📌 Project Overview

Third-party vendors introduce security risks through external software, cloud services, API integrations, sensitive data processing, and privileged system access.

Traditional vendor assessments often rely on manual questionnaires, spreadsheets, and security documentation reviews. These processes can be time-consuming, inconsistent, and difficult to scale.

This project addresses those challenges through two complementary components:

### 1. Third-Party Risk Management Framework

A structured assessment methodology that includes:

- Four vendor criticality tiers
- Tier-specific security questionnaires
- Evidence-based control evaluations
- Weighted risk scoring across six security domains
- Inherent and residual risk assessment methodology
- Risk exception and remediation workflows
- Executive security assessment reporting
- Annual reassessment and continuous monitoring guidance

### 2. Python Vendor Risk Assessment Automation

A Python-based automation module that:

- Reads structured vendor assessment data from JSON
- Validates domain scores and required input fields
- Calculates weighted security risk scores
- Classifies preliminary vendor risk levels
- Identifies missing mandatory security controls
- Flags findings requiring manual security review
- Generates structured JSON assessment reports
- Uses automated unit tests to validate scoring and policy logic

**Security design principle:** A high overall security score does not automatically override a failed mandatory security control.

---

## 🏗️ Framework Architecture

### Third-Party Risk Assessment Lifecycle

```text
                  Vendor Onboarding
                         |
                         v
              Vendor Risk Classification
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
     Critical         High          Medium / Low
      Tier 1          Tier 2          Tier 3 / 4
          |              |              |
          v              v              v
     65 Questions    40 Questions    19 Questions /
      + Audit       + SOC 2 Review   Self-Attestation
          |              |              |
          +--------------+--------------+
                         |
                         v
              Security Control Review
                         |
                         v
               Weighted Risk Scoring
                         |
                         v
              Residual Risk Assessment
                         |
                         v
             Security Risk Recommendation
                         |
              +----------+----------+
              |          |          |
              v          v          v
           Approve   Conditional   Reject /
                     Approval      Exception
                         |
                         v
               Remediation Tracking
                         |
                         v
              Continuous Monitoring
```

### Python Automation Architecture

```text
                 Vendor Assessment Data
                   (sample_vendor.json)
                            |
                            v
                     Input Validation
                            |
              +-------------+-------------+
              |                           |
              v                           v
       Weighted Scoring             Security Policies
         (scoring.py)                (policies.py)
              |                           |
              v                           v
       Risk Classification         Mandatory Control
                                     Validation
              |                           |
              +-------------+-------------+
                            |
                            v
                       main.py
                            |
                            v
                  Assessment Decision
                     Recommendation
                            |
                            v
                  JSON Report Generation
                            |
                            v
                  reports/assessment.json
```

The automation engine provides preliminary assessment recommendations. Final vendor approval and formal risk acceptance remain human-governed decisions.

---

## 📊 Vendor Risk Scoring Model

The framework evaluates vendors across six security domains.

| Security Domain | Weight |
|---|---:|
| Data Security & Encryption | 25% |
| Access Control & Identity Management | 20% |
| Incident Response & Business Continuity | 20% |
| Compliance & Certifications | 15% |
| Network & Infrastructure Security | 10% |
| Physical Security | 10% |
| **Total** | **100%** |

### Weighted Risk Scoring Formula

```text
Weighted Score = Σ (Domain Score × Domain Weight)
```

For example:

```text
Data Security:       84 × 0.25 = 21.00
Access Control:      79 × 0.20 = 15.80
Incident Response:   81 × 0.20 = 16.20
Compliance:          73 × 0.15 = 10.95
Network Security:    78 × 0.10 =  7.80
Physical Security:   95 × 0.10 =  9.50
                              ----------
Final Weighted Score:           81.25/100
```

### Risk Classification

| Weighted Score | Preliminary Risk | Framework Disposition |
|---|---|---|
| 85–100 | Low | Approval review |
| 70–84 | Medium | Conditional approval and remediation |
| 50–69 | High | Conditional approval, 90-day remediation and retesting |
| Below 50 | Critical | Rejection or formal risk exception |

Risk scores are not the sole basis for approval. Data sensitivity, privileged access, mandatory security requirements, compensating controls, and risk acceptance authority must also be considered.

For detailed methodology, see [Vendor Risk Scoring Rubric](risk-scoring/vendor-risk-rubric.md).

---

## 🔐 Mandatory Security Control Validation

The Python automation module includes additional checks for important security requirements.

Current prototype controls:

| Control | Security Objective |
|---|---|
| Privileged MFA | Reduce unauthorized privileged account access |
| Encryption at Rest | Protect stored information |
| Audit Logging | Support monitoring, investigation, and accountability |

If a required control is missing or unverified, the system creates a finding and requires manual security review.

### Example

A vendor receives a weighted security score of **95/100** but does not enforce privileged MFA.

```text
Weighted Score: 95.0
Preliminary Risk: Low

Security Findings:
- Privileged MFA is not enabled

Recommendation:
Manual security review required
```

This prevents a high aggregate score from automatically bypassing important security requirements.

These mandatory checks are prototype policy rules and should be calibrated to the organization's security standards and vendor risk tier.

---

## 📁 Repository Structure

```text
tprm-vendor-risk-framework/
│
├── README.md
│
├── questionnaires/
│   ├── tier1-critical-vendor.md
│   ├── tier2-high-vendor.md
│   ├── tier3-medium-vendor.md
│   └── sample-assessment-acme-cloud-tier2.md
│
├── risk-scoring/
│   └── vendor-risk-rubric.md
│
├── exception-management/
│   └── exception-workflow.md
│
├── templates/
│   └── vendor-risk-report.md
│
├── tprm-visuals/
│
└── automation/
    ├── __init__.py
    ├── main.py
    ├── scoring.py
    ├── policies.py
    ├── Readme.md
    │
    ├── vendor_data/
    │   └── sample_vendor.json
    │
    ├── reports/
    │   └── assessment.json
    │
    └── tests/
        ├── __init__.py
        └── test_scoring.py
```

The generated assessment report is created when the automation runs. Python cache files and other generated artifacts are not required for the project source.

---

## ⚙️ Running the Automated Vendor Risk Assessment

### Prerequisites

- Python 3.10 or later
- Git
- VS Code or another code editor

The current automation uses Python's standard library and does not require third-party Python packages.

### Step 1: Clone the Repository

```bash
git clone https://github.com/jadhavyash/tprm-vendor-risk-framework.git
cd tprm-vendor-risk-framework
```

### Step 2: Review the Vendor Input

Open:

```text
automation/vendor_data/sample_vendor.json
```

Example input:

```json
{
  "vendor_name": "Acme Cloud Demo",
  "vendor_tier": "Tier 2 - High",
  "assessment_type": "Security Assessment",
  "domain_scores": {
    "data_security": 84,
    "access_control": 79,
    "incident_response": 81,
    "compliance": 73,
    "network_security": 78,
    "physical_security": 95
  },
  "controls": {
    "privileged_mfa": false,
    "encryption_at_rest": true,
    "audit_logging": true
  }
}
```

This sample contains fictional demonstration data.

### Step 3: Run the Assessment Engine

From the repository root:

```bash
python -m automation.main
```

### Step 4: Review the Results

Expected output:

```text
===== VENDOR SECURITY ASSESSMENT =====
Vendor: Acme Cloud Demo
Tier: Tier 2 - High
Weighted Score: 81.25
Risk Level: Medium
Findings: 1
Recommendation: Manual security review required
```

The generated report is saved to:

```text
automation/reports/assessment.json
```

The JSON report includes:

- Vendor name and classification
- Assessment timestamp
- Weighted security score
- Preliminary risk level
- Security findings
- Assessment recommendation
- Automated approval status

---

## 🧪 Automated Unit Testing

The project includes Python unit tests covering:

- Perfect security scores
- Weighted score calculations
- Low, Medium, High, and Critical risk classification
- Missing mandatory security controls
- Invalid scoring input
- Missing security domains
- High-scoring vendors with failed mandatory controls

Run the tests from the repository root:

```bash
python -m unittest discover -s automation/tests -v
```

The initial test suite contains 10 test cases.

Testing helps verify that the scoring logic behaves consistently and that important security requirements are not bypassed by a high weighted score.

---

## 📋 Worked Example: Acme Cloud Services

The framework includes a fictional Tier 2 SaaS vendor assessment.

**Vendor:** Acme Cloud Services  
**Service:** SaaS document collaboration platform  
**Vendor Tier:** Tier 2 — High  
**Data Classification:** Confidential  
**Documented Weighted Score:** 81.3/100  
**Inherent Risk:** Medium  
**Final Recommendation:** Conditional Approval

### Identified Security Gaps

| Finding | Security Concern |
|---|---|
| Missing vendor-side DLP | Potential data exfiltration exposure |
| Semiannual access reviews | Access review frequency below the framework requirement |
| Critical vulnerability remediation delays | Longer vulnerability exposure window |
| SOC 2 exceptions | Change-management assurance gaps |

### Recommended Mitigations

- Introduce additional data protection controls
- Establish quarterly access review commitments
- Strengthen critical vulnerability remediation SLAs
- Track SOC 2 exceptions and corrective actions
- Document remediation owners and deadlines
- Perform reassessment based on vendor criticality

The original worked assessment uses the framework's full assessment methodology, including compensating controls and residual-risk considerations.

The automation module's separate sample uses pre-calculated domain scores and is not a full machine-readable conversion of this original assessment.

See [Completed Acme Cloud Vendor Assessment](questionnaires/sample-assessment-acme-cloud-tier2.md).

---

## 📑 Risk Exception Management

Not every vendor will meet all security requirements immediately.

The framework provides a structured process for documenting and reviewing risk exceptions.

Key elements include:

1. Business justification
2. Security risk description
3. Likelihood and impact assessment
4. Compensating controls
5. Authorized risk owner approval
6. Exception expiration date
7. Remediation and reassessment requirements

Exceptions are time-limited and subject to review rather than treated as permanent exemptions from security requirements.

See [Exception Management Workflow](exception-management/exception-workflow.md).

---

## 🚀 Future Engineering Enhancements

The current automation is an initial implementation of the framework's weighted scoring methodology.

Planned enhancements include:

### Questionnaire-Level Scoring

Calculate domain scores directly from individual questionnaire answers rather than requiring manually calculated domain scores.

### Evidence-Based Validation

Track whether evidence is submitted, verified, rejected, or expired. Evidence presence alone should not be treated as proof that a security control is effective.

### Complete Residual Risk Calculation

Implement the original rubric's data sensitivity, privileged access, compensating control, and residual-risk adjustment methodology.

### Streamlit Dashboard

Provide a web interface for uploading vendor assessments, visualizing scores, reviewing findings, and exporting reports.

### Continuous Monitoring

Track remediation deadlines, expiring evidence, policy exceptions, and changes in vendor security posture.

### CI/CD Security Automation

Use GitHub Actions to execute automated tests and validate scoring logic whenever code changes are proposed.

---

## 🎯 Security Engineering Concepts Demonstrated

- Third-Party Risk Management (TPRM)
- Vendor security assessments
- Risk-based security decision-making
- Security control evaluation
- Python security automation
- Input validation and policy checks
- Risk scoring and classification
- Mandatory security control enforcement
- JSON data processing and reporting
- Automated unit testing
- Risk exception management
- Security governance and compliance

---

## ⚠️ Project Scope and Limitations

This is a portfolio and educational security engineering project.

The framework uses fictional vendor assessment data and is not represented as an assessment of real enterprise vendors.

The current Python engine:

- Accepts pre-calculated domain scores
- Does not independently verify security evidence
- Does not automatically assess all questionnaire answers
- Does not fully implement the original residual-risk methodology
- Does not authorize vendor onboarding without human review

The project is intended to demonstrate how documented security risk assessment methodologies can be translated into repeatable automation.

---

## 📚 References

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001)
- [AICPA SOC Reporting Resources](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [Shared Assessments SIG Questionnaire](https://sharedassessments.org/sig/)



*Built to demonstrate the intersection of third-party risk management, security engineering, and practical automation.*
