"""
Problem: 1657 Determine if Two Strings Are Close

Difficulty: Medium

Approach:
Use set to check if both strings have the same unique characters and use Counter to count the frequency of each character. Then compare the sorted frequency counts of both strings.

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""



from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1=set(word1)==set(word2)
        d1=Counter(word1)
        d2=Counter(word2)
        return s1 and sorted(d1.values())==sorted(d2.values())