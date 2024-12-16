# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        queue=deque()
        if not root:
            return root
        
        res=[]
        queue.append(root)
        
        direction=1
        while queue:
            level=deque()
            n=len(queue)
            
            for i in range(n):
                node=queue.popleft()
                if direction==1:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            direction*=-1
        return res