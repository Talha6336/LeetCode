"""
Problem: Greatest Common Divisor of Strings

Difficulty: Easy

Approach:
Use the mathematical property that the GCD of two strings can be found by checking the divisors of their lengths.


Time Complexity: o(n*m) where n and m are the lengths of str1 and str2 respectively.
Space Complexity: O(1) since we are using a constant amount of space for variables.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            fact1, fact2 = len1 // l, len2 // l
            return str1[:l] * fact1 == str1 and str1[:l] * fact2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""