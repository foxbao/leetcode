# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        # 非递归
        stack=[]
        res=[]
        
        stack.append(root)
        
        while len(stack)>0:
            cur=stack.pop()
            if(cur):
                res.append(cur.val)
            else:
                continue
            stack.append(cur.right)
            stack.append(cur.left)
        return res
        
    #     递归    
    #     self.res=[]
    #     if not root:
    #         return []
    #     self.DFS(root)
    #     return self.res
        
    # def DFS(self,root):
    #     if not root: 
    #         return
    #     self.res.append(root.val)
    #     self.DFS(root.left)
    #     self.DFS(root.right)
        
        




        