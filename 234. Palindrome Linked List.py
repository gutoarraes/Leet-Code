# Given the head of a singly linked list, return true if it is a palindrome

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        total = []
        while head:
            total.append(head.val)
            head = head.next
        for i in range(len(total)-1):
            if total[i] != total[len(total)-1-i]:
                return False
        return True
            