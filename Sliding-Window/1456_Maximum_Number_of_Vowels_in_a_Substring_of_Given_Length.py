"""
Problem: Maximum Number of Vowels in a Substring of Given Length

Difficulty: Medium

Approach:
Use a sliding window approach to keep track of the number of vowels in the current substring of length k.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = result = count = 0
        for r in range(len(s)):
            count += 1 if s[r] in vowels else 0
            if r-l+1 > k:
                count -= 1 if s[l] in vowels else 0
                l += 1
            result = max(count, result)
        return result
