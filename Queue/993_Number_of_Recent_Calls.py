"""
Problem: Number of Recent Calls

Difficulty: Easy

Approach:
Use a deque to store the timestamps of the recent calls. When a new call is made, append its timestamp to the deque. Then, remove any timestamps from the front of the deque that are older than 3000 milliseconds from the current timestamp. The length of the deque will give the number of recent calls.

Time Complexity: O(1)
Space Complexity: O(n)
"""


from collections import deque


class RecentCounter:

    def __init__(self):
        self.times = deque()

    def ping(self, t: int) -> int:
        self.times.append(t)
        while self and self.times[0] < t-3000:
            self.times.popleft()
        return len(self.times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
