import unittest
import sys
import io
# Assuming your solution script is named main.py
# If it's named differently, change the import statement below.
import main as main_solution

class TestRecursivePowerSum(unittest.TestCase):

    def setUp(self):
        """Redirect stdin and stdout."""
        self.original_stdin = sys.stdin
        self.original_stdout = sys.stdout
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """Restore stdin and stdout."""
        sys.stdin = self.original_stdin
        sys.stdout = self.original_stdout

    def run_test(self, input_data, expected_output):
        """Helper method to run a test with given input and expected output."""
        sys.stdin = io.StringIO(input_data)
        main_solution.main()
        # Use strip() to remove potential trailing newline added by print
        self.assertEqual(self.captured_output.getvalue().strip(), expected_output)

    def test_sample_cases(self):
        input_data = """2
4
3 -1 1 10
5
9 -5 -5 -10 10"""
        # (-1)^4 = 1
        # (-5)^4 + (-5)^4 + (-10)^4 = 625 + 625 + 10000 = 11250
        expected_output = """1
11250"""
        self.run_test(input_data, expected_output)

    def test_all_positive(self):
        input_data = """1
3
1 2 3"""
        expected_output = "0" # No non-positive numbers
        self.run_test(input_data, expected_output)

    def test_all_negative(self):
        input_data = """1
3
-1 -2 -3"""
        # (-1)^4 + (-2)^4 + (-3)^4 = 1 + 16 + 81 = 98
        expected_output = "98"
        self.run_test(input_data, expected_output)

    def test_mixed_numbers_with_zero(self):
        input_data = """1
5
-2 5 0 -3 10"""
        # (-2)^4 + 0^4 + (-3)^4 = 16 + 0 + 81 = 97
        expected_output = "97"
        self.run_test(input_data, expected_output)

    def test_zero_only(self):
        input_data = """1
2
0 0"""
        # 0^4 + 0^4 = 0
        expected_output = "0"
        self.run_test(input_data, expected_output)

    def test_single_negative(self):
        input_data = """1
1
-4"""
        # (-4)^4 = 256
        expected_output = "256"
        self.run_test(input_data, expected_output)

    def test_mismatch_fewer_numbers(self):
        input_data = """1
5
1 2 3""" # Expected 5 numbers, got 3
        expected_output = "-1"
        self.run_test(input_data, expected_output)

    def test_mismatch_more_numbers(self):
        input_data = """1
2
1 2 3 4""" # Expected 2 numbers, got 4
        expected_output = "-1"
        self.run_test(input_data, expected_output)

    def test_mismatch_empty_yn_line(self):
        input_data = """1
3
""" # Expected 3 numbers, got 0 from empty line
        expected_output = "-1"
        self.run_test(input_data, expected_output)

    def test_multiple_cases_mixed(self):
        input_data = """3
2
-1 -2
4
1 2 3 4
3
0 -10 5"""
        # Case 1: (-1)^4 + (-2)^4 = 1 + 16 = 17
        # Case 2: All positive = 0
        # Case 3: 0^4 + (-10)^4 = 0 + 10000 = 10000
        expected_output = """17
0
10000"""
        self.run_test(input_data, expected_output)

    def test_large_values(self):
        input_data = """1
2
-100 -100"""
        # (-100)^4 + (-100)^4 = 100,000,000 + 100,000,000 = 200,000,000
        expected_output = "200000000"
        self.run_test(input_data, expected_output)

    def test_no_non_positives_case(self):
        input_data = """1
4
1 5 10 99"""
        expected_output = "0"
        self.run_test(input_data, expected_output)

    def test_mismatch_then_valid(self):
        input_data = """2
3
1 2
2
-5 -6"""
        # Case 1: Mismatch (Expected 3, got 2) -> -1
        # Case 2: (-5)^4 + (-6)^4 = 625 + 1296 = 1921
        expected_output = """-1
1921"""
        self.run_test(input_data, expected_output)

    def test_empty_input(self):
        input_data = "" # Completely empty input
        # Expecting no output as EOFError should be caught in main()
        expected_output = ""
        self.run_test(input_data, expected_output)

    # Note: Testing invalid integer inputs (like "abc") is harder
    # because the script's try/except might catch it and default to -1,
    # which could be confused with a mismatch. The current tests focus
    # on the logic specified in the problem description.

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)