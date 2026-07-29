"""
Problem: Delete the Middle Node of a Linked List

Difficulty: Medium

Approach:
Use the slow and fast pointer technique to find the middle node of the linked list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node. Keep track of the previous node to the slow pointer so that we can remove the middle node by updating the next pointer of the previous node.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = prev.next.next

        return head
