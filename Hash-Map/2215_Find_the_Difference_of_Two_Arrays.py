"""
Problem: Find the Difference of Two Arrays

Difficulty: Easy

Approach:
Use two sets to store the unique elements of each array. Iterate through the first set and check if each element is present in the second set. If not, add it to the answer list. Then, convert the second set to a list and return both lists as the final answer.

Time Complexity: O(n)
Space Complexity: O(
"""

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        num1set, num2set = set(nums1), set(nums2)
        ans = []
        for n in num1set:
            if n not in num2set:
                ans.append(n)
            else:
                num2set.remove(n)
        return [ans, list(num2set)]
