# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

# 示例 1：


# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：


# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
 

# 提示：

# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.compare(root.left,root.right)
    
    def compare(self,left,right):
        if left and not right:
            return False
        elif right and not left:
            return False
        elif not left and not right:
            return True
        elif left.val!=right.val:
            return False
        
        outside=self.compare(left.left,right.right)
        inside=self.compare(left.right,right.left)
        isSame=outside and inside
        return isSame

        
        
    