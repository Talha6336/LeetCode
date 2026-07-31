"""
Problem: Reverse Linked List

Difficulty: Easy

Approach:
Use three pointers: prev, curr, and nxt. Initialize prev to None and curr to head. Iterate through the linked list, updating the next pointer of curr to point to prev, then move prev and curr one step forward. Finally, return prev as the new head of the reversed list.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
