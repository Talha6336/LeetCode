"""
Problem: Kids With the Greatest Number of Candies

Difficulty: Easy

Approach:
Use the max function to find the maximum number of candies and then check if each kid can have the greatest number of candies by adding extraCandies.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        max_num = max(candies)
        return [c+extraCandies >= max_num for c in candies]
