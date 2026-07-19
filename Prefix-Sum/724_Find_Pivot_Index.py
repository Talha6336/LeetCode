"""
Problem: Find Pivot Index

Difficulty: Easy

Approach:
Use a variable to keep track of the left sum and calculate the total sum of the array. Iterate through the array, updating the left sum and checking if it is equal to the right sum 

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum=0
        total_sum=sum(nums)
        for i in range(len(nums)):
            if left_sum==total_sum-left_sum-nums[i]:
                return i
            left_sum+=nums[i]
        return -1
        