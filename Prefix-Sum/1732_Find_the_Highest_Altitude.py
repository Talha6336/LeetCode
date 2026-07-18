"""
Problem: Find the Highest Altitude

Difficulty: Easy

Approach:
Use a variable to keep track of the current altitude and another variable to keep track of the maximum altitude. Iterate through the gain array, updating the current altitude and checking if it is greater than the maximum altitude.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        max_altitude = 0
        for change in gain:
            altitude += change
            max_altitude = max(altitude, max_altitude)
        return max_altitude
