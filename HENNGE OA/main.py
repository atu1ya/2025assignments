def main():
    results = []
    try:
        n_str = input()
        n = int(n_str)

        def solve_recursive(count, accumulated_results):
            if count == 0:
                return accumulated_results

            current_result = -1
            try:
                x_str = input()
                x = int(x_str)
                yn_line = input()
                yn_str_list = yn_line.split()
                yn_list = list(map(int, yn_str_list))

                if len(yn_list) != x:
                    current_result = -1
                else:
                    non_positives = filter(lambda y: y <= 0, yn_list)
                    powers_of_four = map(lambda y: pow(y, 4), non_positives)
                    current_result = sum(powers_of_four)

            except (ValueError, EOFError):
                pass

            accumulated_results.append(current_result)
            return solve_recursive(count - 1, accumulated_results)

        all_results = solve_recursive(n, results)
        print('\n'.join(map(str, all_results)))

    except (ValueError, EOFError):
        pass

if __name__ == "__main__":
    main()
