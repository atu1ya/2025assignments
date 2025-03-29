# CITS2200 Lab 1: Sorting and Searching

Name: Atulya Chaturvedi

Student Number: 24225113


## Question 1 (1 mark)
Write a short paragraph explaining the relationship between this problem and more abstract computer science topics we have covered in class.

This problem relates to abstract computer science topics such as sorting, searching and complexity analysis. The leaderboard class requires efficient ordering of the speedrun times, done using merge sort. Additionally the methods submit_run() and count_time() leverage binary search techniques to maintain efficiency. These show the practical applications of referential arrays and algorithms like binary search, merge sort and insertion strategies and query ordered data in an efficient manner.


## Question 2 (1 mark)
What data do you need to store in the `Leaderboard` class?
What algorithm do you intend to use for each method?

The leaderboard class stores a list tuples (time, name), representing speedrun times and their corresponding runner names. This list is always sorted in ascending order of times, with ties broken alphabetically by name. On initialisation, merge sort is used to ensure the leaderboard is ordered. Inestion sort is used to in submit_run to determine the correct position for a new run, followed by list insertion. Rank retrieval in get_rank_time() is done using binary search on the precomputed list of rank transitions. Binary search is used again in get_possible_rank() to determine where new runs may be ranked. Counting occurrences in count_time() will be done using two binary searches to locate the first and last occurrences of a given time, to allow for efficient count calculation.


## Question 3 (5 marks)
Implement your design by filling out the method stubs in `speedrunning.py`.
Your implementation must pass the tests given in `test_speedrunning.py`, which can be invoked by running `python -m unittest`.

See `speedrunning.py`.


## Question 4 (1 mark)
Give an argument for the correctness and complexity of your `__init__()` function.

My `__init__()` function correctly organizes the leaderboard using merge sort, which is perfect for this task since it preserves the order of equal elements (it's "stable"). This stability is crucial when we need to break ties by runner name.

The sorting compares runs in exactly the right way - first by looking at times (faster times come first), and when times are identical, it sorts alphabetically by runner name. This gives us exactly the ordering we need.

For very small inputs (empty or single-element lists), the function simply returns them since they're already sorted. For everything else, it splits the list in half, sorts each part recursively, and then carefully merges them back together.

Time complexity-wise, merge sort follows the T(n) = 2T(n/2) + O(n) pattern, which works out to O(n log n) - much better than simpler sorting algorithms for larger datasets. The space requirements are O(n) for the temporary arrays needed during merging.

## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `submit_run()` function.

The submit_run() function correctly maintains the sorted order of the leaderboard by finding the proper insertion position for a new run. Since the leaderboard is already sorted by time (and alphabetically by name for ties), we can exploit this property to efficiently locate the insertion point.

The function uses binary search to find the correct insertion position. Starting with the entire leaderboard as the search range, it repeatedly compares the midpoint run with the new run. If the midpoint run has a smaller time (or equal time but alphabetically smaller name), we know our insertion point must be after the midpoint. Otherwise, it must be before or at the midpoint. This halves our search space in each iteration.

When the binary search terminates, the low index points to the position where the new run should be inserted to maintain the sorted order - either before the first run with a larger time, or before the first run with the same time but alphabetically larger name.

For complexity, the binary search portion operates in O(log n) time, where n is the number of runs in the leaderboard. However, the actual insertion using Python's list.insert() requires shifting elements to make room, which takes O(n) time in the worst case (when inserting at the beginning of the list). Therefore, the overall time complexity is O(log n + n), which simplifies to O(n).



## Question 6 (1 mark)
Give an argument for the correctness and complexity of your `count_time()` function.

The count_time() function correctly counts occurrences of a specific time in the leaderboard by using binary search to efficiently locate the boundaries of the range where this time appears.

Since the leaderboard is maintained in sorted order by time, all runs with the same time value must appear consecutively in the array. Therefore, to count occurrences, we need only find the first and last indices where the target time appears, then calculate the difference between these positions.

The function implements two specialized binary searches:

find_first() locates the leftmost occurrence by continuing to search left even after finding a match
find_last() locates the rightmost occurrence by continuing to search right after finding a match
For each binary search, we maintain a search range that is halved in each iteration. When comparing the middle element to our target time, we not only determine which half to search next but also update our result variable whenever we find a match. This ensures that even when multiple matches exist, we converge on the boundary positions.

The correctness is guaranteed because binary search will always converge on the correct position in a sorted array, and our modified versions will find the exact boundaries of the range containing our target time.

For complexity, each binary search performs O(log n) comparisons, where n is the number of runs in the leaderboard. Since we perform two binary searches sequentially, the overall time complexity remains O(log n), which is significantly more efficient than a linear scan of O(n) that would be required without binary search.