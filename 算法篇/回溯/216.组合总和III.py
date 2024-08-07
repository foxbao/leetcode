# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

 

# 示例 1:

# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释:
# 1 + 2 + 4 = 7
# 没有其他符合的组合了。
# 示例 2:

# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了。
# 示例 3:

# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res=[]
        self.backtracking(n,k,1,[])
        return self.res
    
    def backtracking(self,target_sum,size,start_idx,path):
        if len(path)==size and sum(path)==target_sum:
            self.res.append(path[:])
            
        for i in range(start_idx,9+1):
            path.append(i)
            self.backtracking(target_sum,size,i+1,path)
            path.pop()
    #     self.res=[]
    #     self.backtracking(target_sum=n,size=k,start_idx=1,path=[])
    #     return self.res
        
    # def backtracking(self,target_sum,size,start_idx,path):
    #     if len(path)==size and sum(path)==target_sum:
    #         self.res.append(path[:])
            
    #     for i in range(start_idx,9+1):
    #         path.append(i)
    #         self.backtracking(target_sum,size,i+1,path)
    #         path.pop()
        
n =6
k = 3

solution=Solution()
print(solution.combinationSum3(k,n))
        
    
            