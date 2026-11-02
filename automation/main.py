
# automation/main.py

import json
from datetime import datetime, timezone
from pathlib import Path

from automation.scoring import calculate_score, classify_risk
from automation.policies import check_controls


# Find the automation folder automatically.
BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "vendor_data" / "sample_vendor.json"
REPORTS_DIR = BASE_DIR / "reports"


def assess_vendor(vendor):
    """
    Perform an automated vendor risk assessment.
    """

    if not isinstance(vendor, dict):
        raise ValueError("Vendor input must be a JSON object")

    required_fields = [
        "vendor_name",
        "vendor_tier",
        "domain_scores",
        "controls"
    ]

    for field in required_fields:
        if field not in vendor:
            raise ValueError(f"Missing required field: {field}")

    if (
        not isinstance(vendor["vendor_name"], str)
        or not vendor["vendor_name"].strip()
    ):
        raise ValueError("Vendor name must be non-empty text")

    if (
        not isinstance(vendor["vendor_tier"], str)
        or not vendor["vendor_tier"].strip()
    ):
        raise ValueError("Vendor tier must be non-empty text")

    # Step 1: Calculate the weighted security score.
    score = calculate_score(vendor["domain_scores"])

    # Step 2: Determine the preliminary risk level.
    risk_level = classify_risk(score)

    # Step 3: Identify missing mandatory controls.
    findings = check_controls(vendor["controls"])

    # Step 4: Recommend the next security review action.
    if findings:
        recommendation = "Manual security review required"
    elif risk_level == "Low":
        recommendation = "Eligible for approval review"
    elif risk_level in ("Medium", "High"):
        recommendation = "Conditional approval review required"
    else:
        recommendation = "Reject or formal exception review"

    # Step 5: Build the assessment report.
    report = {
        "vendor_name": vendor["vendor_name"],
        "vendor_tier": vendor["vendor_tier"],
        "assessment_date": datetime.now(
            timezone.utc
        ).isoformat(),
        "weighted_score": score,
        "preliminary_risk_level": risk_level,
        "findings_count": len(findings),
        "findings": findings,
        "recommendation": recommendation,
        "automated_approval": False
    }

    return report


def main():
    # Load vendor input.
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        vendor = json.load(file)

    # Perform the assessment.
    report = assess_vendor(vendor)

    # Create the reports directory if needed.
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Save the report.
    output_file = REPORTS_DIR / "assessment.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    # Display the result.
    print("\n===== VENDOR SECURITY ASSESSMENT =====")
    print(f"Vendor: {report['vendor_name']}")
    print(f"Tier: {report['vendor_tier']}")
    print(f"Weighted Score: {report['weighted_score']}")
    print(f"Risk Level: {report['preliminary_risk_level']}")
    print(f"Findings: {report['findings_count']}")
    print(f"Recommendation: {report['recommendation']}")
    print(f"\nReport saved to: {output_file}")


if __name__ == "__main__":
    main()
