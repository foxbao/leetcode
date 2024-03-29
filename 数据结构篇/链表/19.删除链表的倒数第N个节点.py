# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

# 示例 1：


# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：

# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：

# 输入：head = [1,2], n = 1
# 输出：[1]
 

# 提示：

# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# 进阶：你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(0, head)
        fast=dummy_head
        slow=dummy_head
        
        for i in range(n+1):
            fast=fast.next

        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy_head.next
        