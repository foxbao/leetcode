# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

# 示例 1：


# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：

# 输入：head = []
# 输出：[]
# 示例 3：

# 输入：head = [1]
# 输出：[1]
 

# 提示：

# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(next=head)
        current = dummy_head
        
        while current.next and current.next.next:
            temp = current.next # 防止节点修改
            temp1 = current.next.next.next
            
            current.next=current.next.next
            current.next.next=temp
            temp.next=temp1
            current=current.next.next
            
        return dummy_head.next
        