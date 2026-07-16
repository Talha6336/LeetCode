"""
Problem: Max Consecutive Ones III

Difficulty: Medium

Approach:
Use the sliding window technique to find the longest subarray with at most k zeros. Maintain a count of zeros in the current window and adjust the left pointer when the count exceeds k.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = zero_count = max_length = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            current_length = r-l+1
            max_length = max(max_length, current_length)
        return max_length
