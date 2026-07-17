"""
Problem: Longest Subarray of 1's After Deleting One Element

Difficulty: Medium

Approach:
Use a sliding window approach to find the longest subarray of 1's after deleting one element. Maintain a count of zeros in the current window and adjust the left pointer when the count exceeds 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = max_length = zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
                while zeros > 1:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
            max_length = max(max_length, r-l+1)
        return max_length-1
