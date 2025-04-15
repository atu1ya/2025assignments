def main():
    """
    Main function that processes input data and generates results.
    Reads input, processes calculations, and outputs results.
    """
    results = []  # List to store results of each test case
    try:
        # Read the number of test cases
        n_str = input()
        n = int(n_str)

        def solve_recursive(count, accumulated_results):
            """
            Recursive function to process each test case.
            
            Args:
                count: Number of remaining test cases to process
                accumulated_results: List of results processed so far
                
            Returns:
                List of results after processing all test cases
            """
            if count == 0:  # Base case: all test cases processed
                return accumulated_results

            current_result = -1  # Default result if processing fails
            try:
                # Read the expected count of numbers for this test case
                x_str = input()
                x = int(x_str)
                
                # Read space-separated numbers and convert to integers
                yn_line = input()
                yn_str_list = yn_line.split()
                yn_list = list(map(int, yn_str_list))

                # Validate that the number of inputs matches the expected count
                if len(yn_list) != x:
                    current_result = -1  # Invalid input: count mismatch
                else:
                    # Calculate sum of fourth powers of non-positive numbers
                    non_positives = filter(lambda y: y <= 0, yn_list)
                    powers_of_four = map(lambda y: pow(y, 4), non_positives)
                    current_result = sum(powers_of_four)

            except (ValueError, EOFError):
                # Handle exceptions from input parsing or calculation
                pass

            # Add result to the accumulated results
            accumulated_results.append(current_result)
            # Process next test case recursively
            return solve_recursive(count - 1, accumulated_results)

        # Start recursive processing with the given number of test cases
        all_results = solve_recursive(n, results)
        # Output all results with each on a new line
        print('\n'.join(map(str, all_results)))

    except (ValueError, EOFError):
        # Handle exceptions from reading the number of test cases
        pass

if __name__ == "__main__":
    main()  # Execute main function when script is run directly
