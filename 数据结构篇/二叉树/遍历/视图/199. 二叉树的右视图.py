# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        if not root:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        while queue:
            n=len(queue)
            level=[]
            for i in range(n):
                node=queue.popleft()
                
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)    
                
            res.append(level[-1])
        return res
        

        