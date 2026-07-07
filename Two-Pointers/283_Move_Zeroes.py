"""
Problem: Move Zeroes

Difficulty: Easy

Approach:
Use two pointers to iterate through the array, moving non-zero elements to the front and filling the rest with zeros.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
