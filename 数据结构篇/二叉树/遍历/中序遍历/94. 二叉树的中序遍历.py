# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 非递归
        stack=[]
        res=[]
        cur=root
        while cur or len(stack)>0:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                res.append(cur.val)
                cur=cur.right
                
        return res

                


    #     # 递归
    #     if not root:
    #         return []

    #     self.res=[]
    #     self.DFS(root)
    #     return self.res
    
    # def DFS(self,root):
    #     if not root:
    #         return
        
    #     self.DFS(root.left)
    #     self.res.append(root.val)
    #     self.DFS(root.right)
        
