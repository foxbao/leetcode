# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return False
        que=collections.deque()
        que.append(root)
        hasNone=False
        while que:
            size=len(que)
            for i in range(size):
                node=que.popleft()
                if not node:
                    hasNone=True
                    continue
                
                if hasNone:
                    return False
                que.append(node.left)
                que.append(node.right)
        return True
                
                
                
        
