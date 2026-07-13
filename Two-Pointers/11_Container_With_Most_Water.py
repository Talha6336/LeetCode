"""
Problem: Container With Most Water

Difficulty: Medium

Approach:

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:

        l = 0
        r = len(height)-1
        result = 0
        while l < r:
            area = (r-l)*min(height[l], height[r])
            result = max(area, result)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return result
