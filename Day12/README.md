Intermediate Problem #9
Problem: Write a function that takes a list of integers and returns a new list where each element is replaced by the product of all other elements in the original list (without using division).

For example, given [1, 2, 3, 4], the function should return [24, 12, 8, 6].

Hints:

Use two passes through the list: one to calculate the product of elements to the left of each index and another for elements to the right.
Multiplying these two products will give the final value for each index.