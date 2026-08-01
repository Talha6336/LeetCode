"""
Problem: 2130 Maximum Twin Sum of a Linked List

Difficulty: Medium

Approach:
Use the slow and fast pointer technique to find the middle of the linked list. Reverse the first half of the linked list while finding the middle. Then, iterate through both halves of the linked list simultaneously to calculate the twin sums and keep track of the maximum twin sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        result = 0
        while slow:
            result = max(result, prev.val+slow.val)
            prev = prev.next
            slow = slow.next

        return result
