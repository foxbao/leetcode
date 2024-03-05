# 给定二叉树的根节点 root ，返回所有左叶子之和。

 

# 示例 1：



# 输入: root = [3,9,20,null,null,15,7] 
# 输出: 24 
# 解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 示例 2:

# 输入: root = [1]
# 输出: 0
 

# 提示:

# 节点数在 [1, 1000] 范围内
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=0
        if not root:
            return 0
        
        self.travel(root,0)
        return self.res
        
    def travel(self,node,isFromLeft):
        if not node:
            return
        
        if not node.left and not node.right and isFromLeft:
            self.res+=node.val
            return
        
        self.travel(node.left,True)
        self.travel(node.right,False)
        
        