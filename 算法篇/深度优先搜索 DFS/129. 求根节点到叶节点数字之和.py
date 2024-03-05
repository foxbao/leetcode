# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root:TreeNode,prevTotal:int)->int:
            if not root:
                return 0
            
            total=prevTotal*10+root.val
            if not root.left and not root.right:
                return
            
            else:
                return dfs(root.left,total)+dfs(root.right,total)
            
        return dfs(root,0)
        