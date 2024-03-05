# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left=self.treeDepth(root.left)
        right=self.treeDepth(root.right)
        if abs(left-right)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def treeDepth(self,root):
        if not root:
            return 0
        
        left=self.treeDepth(root.left)
        right=self.treeDepth(root.right)
        return max(left,right)+1
        