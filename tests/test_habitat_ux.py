#!/usr/bin/env python3
"""
TEST_HABITAT_UX.py

Unit tests for habitat_ux utilities.
"""

import unittest
import sys
import os
import io
import time
from unittest.mock import patch

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from habitat_ux import Spinner, Colors


class TestSpinner(unittest.TestCase):
    """Test Spinner class"""

    def test_spinner_output(self):
        """Test that spinner writes to stdout and cleans up."""
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            with Spinner("Testing...", delay=0.01):
                time.sleep(0.05)
        finally:
            sys.stdout = original_stdout

        output = captured_output.getvalue()

        # Should contain spinner frames
        self.assertIn("⠋", output)
        self.assertIn("Testing...", output)
        # Should contain ANSI colors
        self.assertIn(Colors.CYAN, output)
        # Should contain carriage returns
        self.assertIn("\r", output)

    def test_spinner_context_manager(self):
        """Test that Spinner works as a context manager"""
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with Spinner("Testing..."):
                time.sleep(0.1)

            output = fake_out.getvalue()
            # It should have printed the message and some spinner characters
            self.assertIn("Testing...", output)
            # It should have cleaned up the line
            self.assertIn("\r", output)


class TestColors(unittest.TestCase):
    """Test Colors class"""

    def test_colors_exist(self):
        """Test that Colors class has expected attributes."""
        self.assertTrue(hasattr(Colors, 'HEADER'))
        self.assertTrue(hasattr(Colors, 'BLUE'))
        self.assertTrue(hasattr(Colors, 'CYAN'))
        self.assertTrue(hasattr(Colors, 'GREEN'))
        self.assertTrue(hasattr(Colors, 'YELLOW'))
        self.assertTrue(hasattr(Colors, 'RED'))
        self.assertTrue(hasattr(Colors, 'RESET'))
        self.assertTrue(hasattr(Colors, 'BOLD'))
        self.assertTrue(hasattr(Colors, 'UNDERLINE'))


if __name__ == '__main__':
    unittest.main()
