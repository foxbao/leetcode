# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(cur,prev):
            if not head:
                return prev
            tmp=cur.next
            cur.next=prev
            return reverse(cur=tmp,prev=cur)    
        
        return reverse(head,None)
        
        
        # 双指针
        # if head==None or head.next==None:
        #     return head 
        # cur=head
        # prev=None
        
        # while(cur):
        #     temp=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=temp
            
        # return cur