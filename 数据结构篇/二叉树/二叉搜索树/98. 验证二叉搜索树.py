# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.pre=None
        return self.DFS(root)
        
    def DFS(self,node):
        if not node:
            return True
        
        left=self.DFS(node.left)
        # if node.val>self.maxVal:
        #     self.maxVal=node.val
        # else:
        #     return False
        if self.pre and self.pre.val>=node.val:
            return False
        self.pre=node
        
        right=self.DFS(node.right)
        if left and right:
            return True
        
    #     self.maxVal=float('-int')
    #     return self.DFS(root)
        
    # def DFS(self,node):
    #     if not node:
    #         return True
        
    #     left=self.DFS(node.left)
    #     if node.val>self.maxVal:
    #         self.maxVal=node.val
    #     else:
    #         return False
        
    #     right=self.DFS(node.right)
    #     if left and right:
    #         return True
        
        
        
    #     return self.isValid(root,float('-inf'),float('inf'))
        
    # def isValid(self,root,min,max):
    #     if not root:
    #         return True
        
    #     if root.val>=max or root.val<=min:
    #         return False
        
    #     return self.isValid(root.left,min,root.val) and self.isValid(root.right,root.val,max)