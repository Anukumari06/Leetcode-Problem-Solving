# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if(head==None or head.next==None):
        #     return False
        # slow=head
        # fast=head.next
        # while(slow!=fast):
        #     if(fast==None or fast.next==None):
        #         return False
        # slow=slow.next
        # fast=fast.next.next
        # return True
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False






        # if(head==NULL || head->next==NULL){
        #     return false;
        # }
        # ListNode* slow=head;
        # ListNode* fast=head->next;
        # while(slow!=fast){
        #     if(fast==NULL || fast->next==NULL){
        #         return false;
        #     }
        # slow=slow->next;
        # fast=fast->next->next;
        # }
        # return true;
        