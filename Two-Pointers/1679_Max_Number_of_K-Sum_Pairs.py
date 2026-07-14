"""
Problem: Max Number of K-Sum Pairs

Difficulty: Medium

Approach:
Use two pointers to find pairs of numbers that sum up to k. First, sort the array, then use one pointer starting from the beginning and another from the end. 

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        count = 0
        while l < r:
            current_sum = nums[l]+nums[r]
            if current_sum == k:
                count += 1
                l += 1
                r -= 1
            elif current_sum > k:
                r -= 1
            else:
                l += 1
        return count
