
# automation/scoring.py

# Domain weights based on the existing TPRM framework.
# The weights must total 1.0 (100%).

WEIGHTS = {
    "data_security": 0.25,
    "access_control": 0.20,
    "incident_response": 0.20,
    "compliance": 0.15,
    "network_security": 0.10,
    "physical_security": 0.10,
}


def calculate_score(domain_scores):
    """
    Validate domain scores and calculate a weighted
    vendor security score between 0 and 100.
    """

    if not isinstance(domain_scores, dict):
        raise ValueError("Domain scores must be an object")

    if set(domain_scores.keys()) != set(WEIGHTS.keys()):
        raise ValueError(
            "All six security domains must be provided"
        )

    weighted_score = 0

    for domain, weight in WEIGHTS.items():
        score = domain_scores[domain]

        if (
            type(score) not in (int, float)
            or not 0 <= score <= 100
        ):
            raise ValueError(
                f"Invalid score for {domain}: {score}"
            )

        weighted_score += score * weight

    return round(weighted_score, 2)


def classify_risk(score):
    """
    Convert a weighted score into a preliminary
    risk category.
    """

    if type(score) not in (int, float) or not 0 <= score <= 100:
        raise ValueError("Risk score must be between 0 and 100")

    if score >= 85:
        return "Low"
    elif score >= 70:
        return "Medium"
    elif score >= 50:
        return "High"
    else:
        return "Critical"
