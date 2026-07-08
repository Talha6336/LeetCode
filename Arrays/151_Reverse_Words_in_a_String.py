"""
Problem: Reverse Words in a String

Difficulty: Medium

Approach:
Use the split() method to break the string into words, reverse the list of words, and then join them back together with spaces.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        return " ".join(s)
