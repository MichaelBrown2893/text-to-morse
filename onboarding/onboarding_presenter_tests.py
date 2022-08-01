import io
import sys
import unittest
from . import onboarding_presenter
from . import onboarding_model


class OnboardingTest(unittest.TestCase):
    def test_display_onboarding(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        onboarding_presenter.display_onboarding()
        sys.stdout = sys.__stdout__
        expected = f"{onboarding_model.TITLE}\n" \
                   f"{onboarding_model.WELCOME_MESSAGE}\n" \
                   f"{onboarding_model.INSTRUCTIONS}\n"
        self.assertEqual(captured_output.getvalue(), expected)
