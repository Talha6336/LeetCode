"""
Problem: Product of Array Except Self

Difficulty: Medium

Approach:
Use two passes to calculate the product of all elements except self. In the first pass, calculate the prefix product for each element and store it in the result array. In the second pass, calculate the postfix product and multiply it with the corresponding prefix product in the result array.


Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


