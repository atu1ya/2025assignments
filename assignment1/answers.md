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

The __init__() function ensures correctness by sorting the initial list with merge sort, to acquire the required ranking order. Merge Sort is a sorting algorithm that ensures runs with the same time remain in alphabetical order by name. Merge sort has a recurrence relation of T(n) = 2T(n/2) + O(n), which solves to O(n log n + n). Dropping the lower order term, this leaves the final complexity as O(n log n). 

## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `submit_run()` function.

The submit_run() function correctly inserts new speedruns, while still maintain the sorted order. It uses binary search which has a time complexity of O(log n) to find the correct insertion point. Then to insert the time, there is a complexity O(n) as a worst case, which uses the assumption that every item in the list needs to be moved. This ensures runs remain sorted, and the insertion logic is correct because the binary search finds the first valid position for the new run.


## Question 6 (1 mark)
Give an argument for the correctness and complexity of your `count_time()` function.

The count_time() function correctly coutns occurrences of a given time using two binary searches: one to find the first occurence, and another for the last. Each search operates in O(log n) time, giving a total complexity of O(log n + log n) = O(2 log n). Dropping the constant factor, the final complexity remains O(log n). This ensures efficient lookup compared to a linear scan which would O(n) time.
