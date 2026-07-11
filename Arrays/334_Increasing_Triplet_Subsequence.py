"""
Problem: Increasing Triplet Subsequence

Difficulty: Medium

Approach:
Use two variables to track the smallest and second smallest numbers seen so far. Iterate through the list, updating these variables as needed. If a number greater than both is found, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""



class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False



