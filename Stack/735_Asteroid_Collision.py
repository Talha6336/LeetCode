"""
Problem: Asteroid Collision

Difficulty: Medium

Approach:
Use a stack to keep track of the asteroids. Iterate through each asteroid in the list. If the current asteroid is moving to the right (positive value), push it onto the stack. If it is moving to the left (negative value), check for collisions with the asteroids in the stack. If there is a collision, compare their sizes and determine which asteroid survives. Continue this process until all asteroids have been processed.


Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a+stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack

