#Given head, the head of a linked list, determine if the linked list has a cycle in it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[listNode]) -> bool:
        result = {}
        while head:
            if head in result:
                return True
            else:
                result[head] = True
                head = head.next
        return False