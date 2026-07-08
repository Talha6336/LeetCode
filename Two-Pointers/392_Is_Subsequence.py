"""
Problem: Is Subsequence

Difficulty: Easy

Approach:
Use Two pointer approach to iterate through both strings and check if all characters of s are present in t in the same order.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)



