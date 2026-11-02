
# automation/policies.py

# Prototype mandatory security requirements.
# These rules should be calibrated to the vendor's
# risk tier and the organization's actual policies.

REQUIRED_CONTROLS = {
    "privileged_mfa": "Privileged MFA is not enabled",
    "encryption_at_rest": "Encryption at rest is not enabled",
    "audit_logging": "Audit logging is not enabled",
}


def check_controls(controls):
    """
    Identify mandatory control failures.

    Missing or unconfirmed controls are flagged
    for manual security review.
    """

    if not isinstance(controls, dict):
        raise ValueError("Controls must be an object")

    findings = []

    for control, description in REQUIRED_CONTROLS.items():
        status = controls.get(control)

        if status is not True:
            findings.append({
                "control": control,
                "finding": description,
                "status": (
                    "Failed" if status is False
                    else "Not verified"
                ),
                "requires_review": True
            })

    return findings
