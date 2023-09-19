# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1=""
        prev=head
        while(prev):
            str1+=str(prev.val)
            prev=prev.next
        if(str1==str1[::-1]):
            return True 
        return False