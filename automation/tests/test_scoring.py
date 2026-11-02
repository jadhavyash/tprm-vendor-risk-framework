
# automation/tests/test_scoring.py

import unittest

from automation.scoring import calculate_score, classify_risk
from automation.policies import check_controls
from automation.main import assess_vendor


class TestRiskScoring(unittest.TestCase):

    def test_perfect_score(self):
        scores = {
            "data_security": 100,
            "access_control": 100,
            "incident_response": 100,
            "compliance": 100,
            "network_security": 100,
            "physical_security": 100
        }

        self.assertEqual(calculate_score(scores), 100)

    def test_weighted_score(self):
        scores = {
            "data_security": 84,
            "access_control": 79,
            "incident_response": 81,
            "compliance": 73,
            "network_security": 78,
            "physical_security": 95
        }

        self.assertEqual(calculate_score(scores), 81.25)

    def test_low_risk(self):
        self.assertEqual(classify_risk(90), "Low")

    def test_medium_risk(self):
        self.assertEqual(classify_risk(81.25), "Medium")

    def test_high_risk(self):
        self.assertEqual(classify_risk(60), "High")

    def test_critical_risk(self):
        self.assertEqual(classify_risk(40), "Critical")

    def test_missing_mfa(self):
        controls = {
            "privileged_mfa": False,
            "encryption_at_rest": True,
            "audit_logging": True
        }

        findings = check_controls(controls)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["control"], "privileged_mfa")

    def test_invalid_score(self):
        scores = {
            "data_security": 150,
            "access_control": 79,
            "incident_response": 81,
            "compliance": 73,
            "network_security": 78,
            "physical_security": 95
        }

        with self.assertRaises(ValueError):
            calculate_score(scores)

    def test_missing_domain(self):
        with self.assertRaises(ValueError):
            calculate_score({"data_security": 80})

    def test_high_score_does_not_override_failed_control(self):
        vendor = {
            "vendor_name": "Test Vendor",
            "vendor_tier": "Tier 2",
            "domain_scores": {
                "data_security": 95,
                "access_control": 95,
                "incident_response": 95,
                "compliance": 95,
                "network_security": 95,
                "physical_security": 95
            },
            "controls": {
                "privileged_mfa": False,
                "encryption_at_rest": True,
                "audit_logging": True
            }
        }

        report = assess_vendor(vendor)

        self.assertEqual(report["weighted_score"], 95)
        self.assertEqual(
            report["recommendation"],
            "Manual security review required"
        )
        self.assertFalse(report["automated_approval"])


if __name__ == "__main__":
    unittest.main()
