"""
Problem: Odd Even Linked List

Difficulty: Medium

Approach:
Use two pointers to separate the odd and even indexed nodes. The first pointer (odd) will point to the head of the list, and the second pointer (even) will point to the second node. We will also keep a reference to the head of the even list (even_head). We will iterate through the list, updating the next pointers of the odd and even nodes accordingly. Finally, we will connect the end of the odd list to the head of the even list.


Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = head
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
