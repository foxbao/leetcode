# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

# 如果树中有不止一个众数，可以按 任意顺序 返回。

# 假定 BST 满足如下定义：

# 结点左子树中所含节点的值 小于等于 当前节点的值
# 结点右子树中所含节点的值 大于等于 当前节点的值
# 左子树和右子树都是二叉搜索树
 

# 示例 1：


# 输入：root = [1,null,2,2]
# 输出：[2]
# 示例 2：

# 输入：root = [0]
# 输出：[0]
 

# 提示：

# 树中节点的数目在范围 [1, 104] 内
# -105 <= Node.val <= 105
 

# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre=None
        self.maxCount=float('-inf')
        self.count=0
        self.res=[]
        self.DFS(root)
        return self.res
        
    def DFS(self,node):
        if not node:
            return
        
        self.DFS(node.left)
        
        if not self.pre:
            self.count=1
        elif self.pre.val==node.val:
            self.count+=1
        else:
            self.count=1
            
        self.pre=node
        if self.count==self.maxCount:
            self.res.append(node.val)
        if self.count>self.maxCount:
            self.maxCount=self.count
            self.res=[]
            self.res.append(node.val)
        
        self.DFS(node.right)
        
        
        