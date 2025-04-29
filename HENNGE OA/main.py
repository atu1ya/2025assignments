# Helper function to recursively parse string, validate count, and calculate sum of powers
def calculate_recursive_from_string(s, index, current_num_str, num_count, current_sum_powers):
    """
    Recursively processes a string of space-separated numbers.

    Args:
        s: The input string (assumed stripped of leading/trailing whitespace).
        index: Current position in the string.
        current_num_str: The string representation of the number being built.
        num_count: The count of numbers processed so far.
        current_sum_powers: The accumulated sum of fourth powers of non-positive numbers.

    Returns:
        A tuple (final_count, final_sum). Returns (-999, -999) on parsing error.
    """
    # Base case: end of string
    if index == len(s):
        # Process the last number if any
        if current_num_str:  # Check if there's a number buffered
            try:
                num = int(current_num_str)
                num_count += 1
                if num <= 0:
                    current_sum_powers += pow(num, 4)
            except ValueError:
                 # Indicate parsing error (e.g., "--", or non-numeric parts)
                 return -999, -999
        return num_count, current_sum_powers

    char = s[index]

    if char.isspace():
        # If we encounter a space, process the number accumulated so far
        if current_num_str:  # Check if there's a number buffered
            try:
                num = int(current_num_str)
                num_count += 1
                if num <= 0:
                    current_sum_powers += pow(num, 4)
                # Reset for next number after processing
                current_num_str = ""
            except ValueError:
                 return -999, -999 # Indicate parsing error

        # Continue processing the rest of the string, skipping the space(s)
        # Pass the potentially updated num_count and current_sum_powers
        return calculate_recursive_from_string(s, index + 1, "", num_count, current_sum_powers)
    # Allow '-' only at the start of a number string being built
    elif char == '-' and not current_num_str:
         current_num_str += char
         # Continue processing the rest of the string
         return calculate_recursive_from_string(s, index + 1, current_num_str, num_count, current_sum_powers)
    # Allow digits
    elif char.isdigit():
        current_num_str += char
        # Continue processing the rest of the string
        return calculate_recursive_from_string(s, index + 1, current_num_str, num_count, current_sum_powers)
    else:
        # Invalid character found (not space, not digit, not leading '-')
        return -999, -999 # Indicate parsing error


# Recursive function to process each test case and print the result
def solve_recursive_print(count):
    """
    Recursively processes each test case, calculates the result, and prints it.

    Args:
        count: Number of remaining test cases to process.
    """
    # Base case: all test cases processed
    if count == 0:
        return # Stop recursion

    current_result = -1 # Default result if processing fails or input is invalid
    try:
        # Read the expected count of numbers for this test case
        x_str = input()
        # Handle potential empty input for x
        if not x_str.strip():
             raise ValueError("Empty input for x")
        x = int(x_str)
        # Assuming count cannot be negative
        if x < 0:
             raise ValueError("Negative count x")

        # Read the line containing space-separated numbers
        yn_line = input()
        yn_line_stripped = yn_line.strip()

        # Process based on expected count x
        if x == 0:
             # If expecting 0 numbers, the line should be empty or whitespace
             if not yn_line_stripped:
                 final_count = 0
                 final_sum = 0
             else:
                 # Line not empty, but expected 0 numbers -> mismatch
                 final_count = -1 # Use count mismatch logic below
                 final_sum = 0
        elif not yn_line_stripped:
             # If expecting > 0 numbers, but line is empty -> mismatch
             final_count = -1 # Use count mismatch logic below
             final_sum = 0
        else:
             # Process non-empty line for x > 0 using the recursive helper
             final_count, final_sum = calculate_recursive_from_string(yn_line_stripped, 0, "", 0, 0)

        # Determine current_result based on processing outcome
        if final_count == -999: # Check for parsing error signal
            current_result = -1
        elif final_count != x:
            current_result = -1  # Invalid input: count mismatch
        else:
            current_result = final_sum

    except (ValueError, EOFError):
        # Handle exceptions from reading x, yn_line, or int conversion of x
        # Also catches errors raised for invalid x values
        current_result = -1 # Ensure result is -1 on any error during case processing

    # Print the result for the current test case
    print(current_result)

    # Process the next test case recursively
    solve_recursive_print(count - 1)


def main():
    """
    Main function: reads the number of test cases and initiates recursive processing.
    Handles initial input reading errors.
    """
    try:
        # Read the number of test cases
        n_str = input()
        # Handle potential empty input for n
        if not n_str.strip():
             raise ValueError("Empty input for n")
        n = int(n_str)
        # Assuming number of test cases cannot be negative
        if n < 0:
             raise ValueError("Negative count n")

        # Start recursive processing only if n > 0
        if n > 0:
             solve_recursive_print(n)
        # If n is 0, the program should produce no output, which happens naturally.

    except (ValueError, EOFError):
        # Handle exceptions from reading n or int conversion.
        # Per typical competitive programming, errors reading 'n' often mean
        # no output should be produced, so we just pass.
        pass

if __name__ == "__main__":
    main() # Execute main function when script is run directly
