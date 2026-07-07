"""
Problem: Reverse Vowels of a String

Difficulty: Easy

Approach:
Use two pointers to iterate through the string from both ends, swapping vowels when found.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)

