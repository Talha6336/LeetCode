"""
Problem: Maximum Average Subarray I

Difficulty: Easy

Approach:
Use a sliding window of size k to calculate the sum of the first k elements, then slide the window across the array, updating the sum and keeping track of the maximum sum found.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        for i in range(len(nums)-k):
            curr_sum += nums[i+k]-nums[i]
            max_sum = max(curr_sum, max_sum)

        return max_sum/k


print(Solution.findMaxAverage(Solution(), [1, 12, -5, -6, 50, 3], 4))
