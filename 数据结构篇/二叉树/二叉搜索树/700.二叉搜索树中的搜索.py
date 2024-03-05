# 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

 

# 示例 1:


# 输入：root = [4,2,7,1,3], val = 2
# 输出：[2,1,3]
# 示例 2:


# 输入：root = [4,2,7,1,3], val = 5
# 输出：[]
 

# 提示：

# 树中节点数在 [1, 5000] 范围内
# 1 <= Node.val <= 107
# root 是二叉搜索树
# 1 <= val <= 107

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        while root:
            if val<root.val:
                root=root.left
            elif val>root.val:
                root=root.right
            else:
                return root
        return None
        
        
    # #DFS递归
    #     return self.DFS(root,val)
        
    # def DFS(self,node,val):
    #     if not node or node.val==val:
    #         return node
        
    #     result=TreeNode()
    #     if val<node.val:
    #         result=self.DFS(node.left,val)
    #     elif val>node.val:
    #         result=self.DFS(node.right,val)
            
    #     return result
        
    
        
        