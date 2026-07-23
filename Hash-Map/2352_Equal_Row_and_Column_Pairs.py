"""
Problem: Equal Row and Column Pairs

Difficulty: Medium

Approach:
Use a dictionary to count the occurrences of each row in the grid. Then, for each column, create a tuple representation and check if it exists in the dictionary. If it does, add the count of that row to the total pairs.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""



from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        pairs = 0
        n = len(grid)
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            if column in rows:
                pairs += rows[column]
        return pairs
