"""
Problem: Merge Strings Alternately

Difficulty: Easy

Approach:
Use two pointers to iterate through both strings simultaneously.

Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if 1 <= len(word1) and len(word2) <= 100:
            i, j = 0, 0
            merged = []
            while i < len(word1) and j < len(word2):
                merged.append(word1[i])
                merged.append(word2[j])
                i += 1
                j += 1
            merged.append(word1[i:])
            merged.append(word2[j:])
        return "".join(merged)
