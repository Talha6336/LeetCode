"""
Problem: Unique Number of ccurrences

Difficulty: Easy

Approach:
Use a dictionary to count the frequency of each number in the array. Then, check if the length of the frequency dictionary is equal to the length of the set of its values.


Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq_count = {}
        for item in arr:
            freq_count[item] = freq_count.get(item, 0)+1

        return len(freq_count) == (len(set(freq_count.values())))
