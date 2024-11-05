# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

 

# 示例 1：
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        self.DFS(root)
        return root
    
    def DFS(self,root):
        if not root:
            return
        
        tmp=root.left
        root.left=root.right
        root.right=tmp
        
        self.DFS(root.left)
        self.DFS(root.right)
        
        
        
        

solution=Solution()
height=[4,2,7,1,3,6,9]
print(solution.invertTree(height))

