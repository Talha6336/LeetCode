"""
Problem: Dota2 Senate

Difficulty: Medium

Approach:
Use two deques to keep track of the indices of the senators from each party. In each round, compare the indices of the senators from both parties. The senator with the lower index gets to ban the other senator, and the banned senator is removed from the game. The winning senator's index is updated by adding the length of the senate to it, so they will get another turn in the next round. Continue this process until one party has no senators left.

Time Complexity: O(n)
Space Complexity: O(n)
"""



from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        D,R=deque(),deque()
        for i,c in enumerate(senate):
            if c=='R':
                R.append(i)
            else:
                D.append(i)
        while D and R:
            dturn=D.popleft()
            rturn=R.popleft()

            if rturn < dturn:
                R.append(dturn+len(senate))
            else:
                D.append(rturn+len(senate))

        return 'Radiant' if R else 'Dire'