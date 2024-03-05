# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

# 你可以按 任何顺序 返回答案。

 

# 示例 1：

# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# 示例 2：

# 输入：n = 1, k = 1
# 输出：[[1]]
 

# 提示：

# 1 <= n <= 20
# 1 <= k <= n

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res=[]
        
        def backtracking(n,k,start_idx,path):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(start_idx,n+1):
                path.append(i)
                backtracking(n,k,i+1,path)
                path.pop()
        
        backtracking(n,k,1,[])
        return res
        
        
        
n = 4
k = 2

solution=Solution()
print(solution.combine(n,k))