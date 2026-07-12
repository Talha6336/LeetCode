"""
Problem: String Compression

Difficulty: Medium

Approach:
Use two pointers to iterate through the list of characters. Count consecutive characters and replace them with the character followed by its count if greater than 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        count = 1
        for j in range(1, len(chars)+1):
            if j < len(chars) and chars[j] == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for k in str(count):
                        chars[i] = k
                        i += 1
                count = 1
        return i
