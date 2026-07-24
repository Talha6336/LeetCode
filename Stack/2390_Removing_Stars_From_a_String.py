"""
Problem: Removing Stars From a String

Difficulty: Medium

Approach:
Use a stack to keep track of the characters in the string. Iterate through each character in the string. If the character is not a star, push it onto the stack. If the character is a star, pop the top character from the stack (if the stack is not empty). Finally, join the characters in the stack to form the resulting string.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack and stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
