Intermediate Problem #18

Problem: Write a function that takes a list of integers and a target integer and returns all unique triplets in the list that add up to the target. Each triplet should be sorted, and the output should not contain duplicate triplets.

For example:

    For the input nums = [-1, 0, 1, 2, -1, -4] and target = 0, the output should be [[-1, -1, 2], [-1, 0, 1]].

Hints:

    Sort the list first.
    Use a two-pointer technique to find pairs that, combined with the current number, add up to the target.
    Avoid duplicates by skipping over numbers that are the same as the previous one.