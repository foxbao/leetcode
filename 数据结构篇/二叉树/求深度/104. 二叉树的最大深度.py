# 给定一个二叉树 root ，返回其最大深度。

# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

 

# 示例 1：



 

# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 示例 2：

# 输入：root = [1,null,2]
# 输出：2
 

# 提示：

# 树中节点的数量在 [0, 104] 区间内。
# -100 <= Node.val <= 100
# 请问您在哪类招聘中遇到此题？
# 1/5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #后序遍历
        if not root:
            return 0
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        
        return max(left,right)+1
    