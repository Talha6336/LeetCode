"""
Problem: 394 Decode String

Difficulty: Medium

Approach:
Use stack to keep track of characters and numbers. Iterate through each character in the string. If the character is not ']', push it onto the stack. If it is ']', pop characters from the stack until you find the matching '['. Then, pop digits from the stack to get the multiplier for the substring. Finally, push the repeated substring back onto the stack. Continue this process until all characters have been processed.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop()+substr
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                stack.append(int(k) * substr)
        return ''.join(stack)
