# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：

# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。

# 叶节点 是指没有子节点的节点。

 

# 示例 1：

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
        