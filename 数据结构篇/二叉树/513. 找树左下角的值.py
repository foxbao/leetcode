# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

# 假设二叉树中至少有一个节点。

 

# 示例 1:



# 输入: root = [2,1,3]
# 输出: 1
# 示例 2:



# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
 

# 提示:

# 二叉树的节点个数的范围是 [1,104]
# -231 <= Node.val <= 231 - 1 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        self.max_depth=0
        self.result=-1
        self.DFS(root,1)
        return self.result
        
    def DFS(self,node,depth):
        if not node.left and not node.right:
            if depth>self.max_depth:
                self.max_depth=depth
                self.result=node.val
        
        if node.left:
            depth+=1
            self.DFS(node.left,depth)
            depth-=1
            
        if node.right:
            depth+=1
            self.DFS(node.right,depth)
            depth-=1
            
        