# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get the values from the current nodes or 0 if None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10

            # Create new node with the current digit
            current.next = ListNode(total % 10)

            # Move to the next node in the result list
            current = current.next

            # Move to the next nodes in l1 and l2, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
