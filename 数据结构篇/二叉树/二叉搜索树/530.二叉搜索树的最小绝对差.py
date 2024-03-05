# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

# 差值是一个正数，其数值等于两值之差的绝对值。

 

# 示例 1：


# 输入：root = [4,2,6,1,3]
# 输出：1
# 示例 2：


# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
 

# 提示：

# 树中节点的数目范围是 [2, 104]
# 0 <= Node.val <= 105

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('inf')
        self.pre=None
        self.DFS(root)
        return self.result
        
    def DFS(self,cur_node):
        if not cur_node:
            return
        
        self.DFS(cur_node.left)
        
        if self.pre:
            self.result=min(self.result,cur_node.val-self.pre.val)
            
        self.pre=cur_node
        
        self.DFS(cur_node.right)
        