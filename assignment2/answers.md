# CITS2200 Lab 2: Genealogy

Name: ATULYA CHATURVEDI

Student Number: 24225113


## Question 1 (1 mark)
Write a simple description of how you are going to represent the problem as a data structure.
Your description should justify how the representation is going to help you solve the problem within the target complexities.

I chose to represent the problem using a tree data structure, where each node in the tree (_Individual class) represents a person with:
- A name (string)
- A reference to their parent
- A list of children (ordered by age, with eldest first)

## Question 2 (1 mark)
Write a simple description of the algorithm you have designed for `get_cousin_dist()`.
Your description should justify the correctness of your algorithm, and make an argument as to its time complexity.

The algorithm for get_cousin_dist() works by finding the path from the originator to each of the two individuals using parent references, then identifies the most recent common ancestor by comparing paths, calculates the number of generations (order) of each individual relative to the most recent common ancestor. This degree is the minimum of the two orders, and the removal is the absolute difference between the orders. The algorithm is correct as it accurately identifies common ancestries by tracing paths in the tree, and the removal calculation captures the generational difference between cousins and the degree calculation follows the definition of cousin relationships. 

The algorithm takes O(n) time. This is due to thhe fact that finding the path from each individual to the originator takes O(n) time where n is the height of the tree, as each step follows one parent reference upward (O(1) per step), and as such in the worst case the maximum number of steps is the depth of the node. 
Then comparing paths takes O(n) time as both paths are iterated through simultaneously and the maximum length of comparison is the shorter path length (at most n). 
Comparing orders, degree and removal takes O(1) time. 
Therefore the total time complexity is O(n) + O(n) + O(1) time. Dropping lower order terms gives us the time complexity as O(n) 


## Question 3 (5 marks)
Implement your design by filling out the method stubs in the `Genealogy` class found in `genealogy.py`.
You are **not** allowed to import any modules.
Your implementation must pass the tests given in `test_genealogy.py`, which can be invoked by running `python -m unittest`.

See `genealogy.py`.


## Question 4 (1 mark)
Give an argument for the correctness and complexity of your `get_primogeniture_order()` function.

The function implements a depth-first traversal of the tree to ensure that each parent is followed by their eldest child and all descendants before proceeding to the next sibling. The depth first approact correctly models primogeniture succession, where the line of succession passes to the eldest child and their descendants before moving to the next sibling, and by adding children to the stack in reverse order, it ensures that the eldest children are processed first. This produces pre-order traversal where each node is visited before its descendants, matching the primogeniture principle.

It takes O(1) time to create the initial stack with the originator, and each node is processed exactly once in the main loop. For each node, the pop operation takes O(1) time, the time to append to result list takes O(1) time, and adding children to the stack takes O(n) time, where n is the number of children. 
Since each node is traversed once, the total operations are proportional to the sum of the number of individuals and the number of parent-child relationships. Thus the time complexity is O(n) since the number of parent child relationships will always be smaller than the number of individuals. 


## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `get_seniority_order()` function.

The get_seniority_order() function uses a breadth-first traversal of the tree, proccessing all individuals at a generation before moving to the next. The breadth-first approach makes sure that proximity to the originator is prioritised, and by using a queue and adding children by order of age in descending order, it is guaranteed that older siblings come before younger ones. 

It takes O(1) time to create the initial queue with the originator, and the main loop is processed exactly once, thus for each node the dequeue operation takes O(1) time, appending to result list takes O(1) time and adding children to queue takes O(n) time where n is the number of children. The total operations are proportional to the sum of the number of individuals and the number of parent child relationships. Therefore the time complexity is O(n) since the number of parent child relationships will always be smaller than the number of individuals.


## Question 6 (1 mark)
Give a brief explanation of the function and purpose of any data structures you implemented.

1. Tree structure (_Indivudal class):
    This represents the hierarchical genealogical relationships, allowing tracing of lineage, identification of ancestors and descendants with each node storing its name, parent reference and children list.
    Node creation takes O(1) time, adding a child takes O(1) time to append to the children list and accessing a parent takes O(1) time.

2. Dictionary (individuals in Genealogy class):
    This provides fast access to any individual by name, enabling O(1) lookups of individuals without traversing the tree and maps individual naems (strings) to their corresponding _Individual objects.
    Lookup takes O(n) in the worst case, insertion takes O(1) time and the dictionary enables O(1) access to any individual that would otherwise need O(n) tree traversal.

3. Stack (in get_primogeniture_order()):
    The stack allows for depth-first traversal, maintaining the order of nodes to be processed next, ensuring eldest-first processing. 
    Push takes O(1) time, pop takes O(1) time as well.

4. Queue (in get_seniority_order()):
    The queue allows for breadth-first traversal, processing individuals level by level, maintaining generational boundaries. 
    Enqueue takes O(1) time, Dequeue takes O(1) time as well.

Any nested operations such as dictionary lookups withing tree traversals still maintain the overall stated complexities due to the fact that the dominant factor is still the number of nodes being processed.