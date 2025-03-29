In labs for this unit, we aim for you to get some practise with the process of analysing, solving, and explaining a computer science problem.
Eventually we expect you should be able to solve these problems unaided, but in these labs we will provide guidance and milestones, with the intention being that you fill the specified gaps.

You are encouraged to discuss these problems with your classmates, though anything you submit for assessment must be your own original work.
Your writings should be from your own understanding, not paraphrased from an external source.
Your code must be your own, and you should understand the decision process behind why you implemented the code as you did.



# CITS2200 Lab 1: Speedrunning Leaderboard

To help you through the problem solving process we have broken it down into the following stages:
- Description
- Abstraction
- Investigation
- Design
- Implementation
- Analysis

You will only be assessed on some of these stages, but you are strongly encouraged to make sure you understand the whole process.
Having said this, problem solving is a highly flexible exercise with no universally perfect process, and this is meant only as a teaching aid, not as a strict framework.
So long as you are comfortable tackling all the aspects of the problem solving process, you are not expected to follow any particular framework.


## Description

You are tasked to design a class for keeping track of a speedrunning leaderboard, ranked by fastest run using [standard competition ranking](https://en.wikipedia.org/wiki/Ranking#Standard_competition_ranking_(%221224%22_ranking)).
Your class must implement certain functionalities.
Specifically we wish to be able to:
1. Get the current leaderboard (in rank order) at any time
2. Submit a new run with a given time and runner name to the leaderboard
3. Construct a new instance of the class given an initial list of runs
4. Find the run time required to achieve a given rank
5. Find what rank a particular time would achieve if submitted
6. Find how many runs are tied for a given time

You will be asked to implement this as the `Leaderboard` class found in `speedrunning.py`.
You are **not** allowed to use Python's built-in sorting functions or import any modules.


## Abstraction

**Question 1 (1 mark):**
Write a short paragraph explaining the relationship between this problem and more abstract computer science topics we have covered in class.

Write your answer in the space provided in `answers.md`.


## Investigation

Hint: Above you should have been able to argue that this problem can be abstracted to sorting, updating, and searching ordered lists.

Now we can investigate the properties of this more abstract concept and algorithms and data structures for working with ordered lists.
Specifically, you should investigate and understand the logic behind insertion sort, merge sort, and binary search.
These have already been covered in Exercise 1, and if you have not yet completed this exercise, you are encouraged to do so now.


## Design

Armed with the understanding you developed in your investigation, you should now be able to come up with a design for how to solve this problem.

Reminder: You are **not** allowed to use Python's built-in sorting functions or import any modules.

**Question 2 (1 mark):**
What data do you need to store in the `Leaderboard` class?
What algorithm do you intend to use for each method?

Write your answer in the space provided in `answers.md`.


## Implementation

**Question 3 (5 marks):**
Implement your design by filling out the method stubs in `speedrunning.py`.
Your implementation must pass the tests given in `test_speedrunning.py`, which can be invoked by running `python -m unittest`.

Reminder: You are **not** allowed to use Python's built-in sorting functions or import any modules.

You are welcome to add methods to the class, so long as they do not compromise the provided tests.


## Analysis

You should at this point be confident in your implementation, and should be able to explain the logic behind how it works to others.

The following questions ask you to provide arguments explaining your design.
Only brief, informal arguments are required of about a paragraph each.
You should not simply cite the known complexity for the algorithm you have chosen, nor should you simply narrate the code step by step, as this only explains *what* the algorithm does, not *why* it is correct.
Your arguments should be sufficient to convince a fellow student who has not seen this algorithm before that your design is correct and has the complexity you claim.

As a very simple example, here is an acceptable argument for the correctness and complexity of using binary search to find the largest natural number `x` such that `x^2 < y` for some given natural number `y`:
> Since the square of any natural number cannot be smaller than that number, we know that `y` can not be smaller than `x`.
> Therefore any answer must exist in the range between `0` and `y`.
> Using binary search, we can refine this range by taking the midpoint `m` of the range, comparing `m^2` to `y`.
> If `m^2 < y`, then we know that `m` satisfies `x^2 < y`, and so `x` must be at least `m`.
> Otherwise `m` must not satisfy the constraint, and so `x` must be less than `m`.
> Either way, this allows us to halve the search range.
> Repeating this process will eventually leave us with a range containing a single integer, which must therefore be the answer.
> Each step halves the size of the range, which started at `y`, meaning that it will take at most `log2(y)` steps to cut the range down to a single integer.
> Since each step can be done in constant time, this gives a time complexity of `O(lg y)`.

**Question 4 (1 mark):**
Give an argument for the correctness and complexity of your `__init__()` function.

**Question 5 (1 mark):**
Give an argument for the correctness and complexity of your `submit_run()` function.

**Question 6 (1 mark):**
Give an argument for the correctness and complexity of your `count_time()` function.

Write your answers in the spaces provided in `answers.md`.


## Extension

Consider the following questions:
1. Give arguments for the correctness and complexity of every method.
2. Is there a tradeoff between the complexities of different methods? That is, does making one method faster necessitate making another slower?
3. How could you make `get_runs()` tie-break by submission order instead of by name?



# Assessment

This lab is marked out of 10 marks and is worth 10% of your unit mark.

## Submitting

Submit only `speedrunning.py` and `answers.md` to cssubmit.
Ensure your name and student number are in the spaces provided at the top of both files.

## Marking Rubric

Each assessable component of this lab relates to some of the learning outcomes for this unit.
For reference, the learning outcomes for this unit are that students should be able to:
1. Undertake problem identification via abstraction
2. Describe common and important data structures and algorithms in the computing discipline
3. Implement a range of data structures and information literacy algorithms in a high-level programming language
4. Apply existing data structures and algorithms from pre-built software libraries
5. Design data structures and algorithms
6. Critically assess the performance of different data structures and algorithms

| Question | Basic                                              | Proficient                 | Total | Outcomes |
| -------- | -------------------------------------------------- | -------------------------- | ----- | -------- |
| 1        | (+1) Relates problem description to abstract topic |                            | /1    | 1        |
| 2        | (+1) Proposes a valid design                       |                            | /1    | 2, 5, 6  |
| 3        | (+1) Passes at least 50% of provided unit tests    | (+4) Passes all unit tests | /5    | 2, 3     |
| 4        | (+1) Provides convincing argument                  |                            | /1    | 2, 6     |
| 5        | (+1) Provides convincing argument                  |                            | /1    | 2, 6     |
| 6        | (+1) Provides convincing argument                  |                            | /1    | 2, 6     |
