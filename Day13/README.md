Intermediate Problem #10
Problem: Write a function that takes a list of integers and returns the longest contiguous subarray with a sum that is equal to zero. If there are multiple subarrays with the same length, return any of them.

Hints:

You can use a dictionary to track cumulative sums at each index.
If a cumulative sum repeats, the subarray between the indices of those two sums has a sum of zero.