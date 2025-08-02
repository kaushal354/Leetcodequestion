# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # This comparison logic is still needed for tie-breaking
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        # 1. Initialize a PriorityQueue
        pq = PriorityQueue()
        head = tail = ListNode(0)

        # 2. Populate the PriorityQueue with initial nodes
        for node in lists:
            if node:
                pq.put((node.val, node))

        # 3. Build the merged list
        while not pq.empty():
            # Get the node with the smallest value (highest priority)
            val, node = pq.get()
            
            tail.next = node
            tail = tail.next
            
            if node.next:
                # Add the next node from the same list into the queue
                pq.put((node.next.val, node.next))

        # 4. Return the result
        return head.next
        
                
            

        
        