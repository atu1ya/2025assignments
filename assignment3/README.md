In labs for this unit, we aim for you to get some practise with the process of analysing, solving, and explaining a computer science problem.
Eventually we expect you should be able to solve these problems unaided, but in these labs we will provide guidance and milestones, with the intention being that you fill the specified gaps.

You are encouraged to discuss these problems with your classmates, though anything you submit for assessment must be your own original work.
Your writings should be from your own understanding, not paraphrased from an external source.
Your code must be your own, and you should understand the decision process behind why you implemented the code as you did.



# CITS2200 Lab 6

From previous labs you should now have some experience with the problem solving process.
In this lab, we simply give you two problems to solve, and want to see the solutions you end up with.

**Note:**
Both problems award a mark for reaching the specified target complexity, but more marks for providing convincing explanations of correctness and complexity.
Therefore you are encouraged to make sure you clearly understand any solution you submit, as you will get more marks for explaining a slower algorithm than for using a faster algorithm you are unable to explain.



# CITS2200 Lab 6A: Trains and Planes

## Description

The European Union is in the process of constructing new stretches of high-speed rail in order to reduce dependence on short-haul flights.

As new high-speed rail lines become available, it will become possible to replace some flights with rail journeys.
EU authorities would like your help figuring out which flights are no longer necessary.

You have been given two lists.
The first is a list of rail lines specified by the cities they connect and the first date from which service runs along that line.
The second is a list of flights specified by flight number, date, departure city and arrival city.

A flight can be replaced by a rail journey if, on the day of the flight, there is any series of high-speed rail lines connecting the departure city to the arrival city, no matter how circuitous the root may be.

Return a list of flights (in the same format as they were given) that could be replaced by a rail journey.


## Implementation

**Question 1 (3 marks):**
Implement your solution by filling out the method stub in the in `trains_planes.py`.
You **may** import and use any **built-in python module** (but no external libraries).
You may write any support functions or classes you require in `trains_planes.py`.

**Note:**
One mark is allocated for achieving the target complexity of `O(N lg N)`, where `N = len(trains) + len(planes)` is the size of the input.


## Analysis

**Question 2 (1 mark):**
Give an argument for the correctness of your `trains_planes()` function.

**Question 3 (1 mark):**
Give an argument for the complexity of your `trains_planes()` function.

Write your answers in the spaces provided in `answers.md`.


## Extension

Consider the following questions:
1. What if we knew the lengths of each rail trip and each flight, and only considered flights replacable if there was a rail journey at most `k` times longer?
2. Given a list of possible new rail lines, with lengths, could you select which one is best to build to minimize the average rail journey length between every pair of cities?



# CITS2200 Lab 6B: Security Routing

## Description

The speedrunners are back, but this time they want your help with figuring out the optimal route to take in a game.

The game level consists of a number of rooms connected by doors and corridors.
Some doors require a certain colour (Red, Green, or Blue) security clearance to get through.
In some of the rooms, there are security stations, some of which can reprogram the player's clearance to a specific colour, if the player so chooses.

The player starts standing at a specified security station, and must reach a designated security station to finish the level.

A segment is a part of a speedrun that has already been optimized.
In this case, the speedrunners already know the fastest ways to get from one security station to another for some pairs of stations.
Some of these segments require a particular security clearance, however, and so require you to collect that clearance at a station before you are able to use that segment.

Every security station has been assigned an integer ID.
A segment is specified by the station it starts at, the station it ends at, how long it takes, and what clearance (if any) is required along the way.
You are given a list of the colour each security station can reprogram your clearance to (if any), a list of the best segments the speedrunners know, and the IDs of the source and target stations.

They would like your help finding the fastest possible route from the source station to the target station.
Can you figure out how long the fastest possible route takes to run?


## Implementation

**Question 4 (3 marks):**
Implement your solution by filling out the method stub in the in `security_routing.py`.
You **may** import and use any **built-in python module** (but no external libraries).
You may write any support functions or classes you require in `security_routing.py`.


**Note:**
One mark is allocated for achieving the target complexity of `O(N lg N)`, where `N = len(stations) + len(segments)` is the size of the input.


## Analysis

**Question 5 (1 mark):**
Give an argument for the correctness of your `security_route()` function.

**Question 6 (1 mark):**
Give an argument for the complexity of your `security_route()` function.

Write your answers in the spaces provided in `answers.md`.


## Extension

Consider the following questions:
1. Could you provide a possible optimal route, rather than just its length?
2. Could you provide a list of all possible optimal routes?



# Assessment

This lab is marked out of 10 marks and is worth 10% of your unit mark.

## Submitting

Submit only `trains_planes.py`, `security_routing.py`, and `answers.md` to cssubmit.
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

| Question | Basic                                              | Proficient                 | Advanced                            | Total | Outcomes      |
| -------- | -------------------------------------------------- | -------------------------- | ----------------------------------- | ----- | ------------- |
| 1        | (+1) Passes at least 50% of provided unit tests    | (+1) Passes all unit tests | (+1) Achieves the target complexity | /3    | 2, 3, 4, 5, 6 |
| 2        | (+1) Provides convincing argument                  |                            |                                     | /1    | 1, 2, 5       |
| 3        | (+1) Provides convincing argument                  |                            |                                     | /1    | 6             |
| 4        | (+1) Passes at least 50% of provided unit tests    | (+1) Passes all unit tests | (+1) Achieves the target complexity | /3    | 2, 3, 4, 5, 6 |
| 5        | (+1) Provides convincing argument                  |                            |                                     | /1    | 1, 2, 5       |
| 6        | (+1) Provides convincing argument                  |                            |                                     | /1    | 6             |
