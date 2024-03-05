# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用 一次 。

# 注意：解集不能包含重复的组合。 

 

# 示例 1:

# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 示例 2:

# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
 

# 提示:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#没写完去重，要重看  
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res=[]
        candidates.sort()
        used=[False]*len(candidates)
        self.backtracking(candidates=candidates,start_idx=0,path=[],sum=0,target=target,used=used)
        return self.res
        
    def backtracking(self,candidates,start_idx,path,sum,target,used):
        if path==[1,1,6]:
            aaa=1
        if sum>target:
            return
        if sum==target:
            self.res.append(path[:])
            return
            
        for i in range(start_idx,len(candidates)):
            if i>start_idx and candidates[i]==candidates[i-1] and not used[i-1]:
                continue
                
            path.append(candidates[i])
            sum+=candidates[i]
            used[i]=True
            self.backtracking(candidates=candidates,start_idx=i+1,path=path,sum=sum,target=target,used=used)
            used[i]=False
            path.pop()
            sum-=candidates[i]
        
solution=Solution()
candidates=[10,1,2,7,6,1,5]
target=8
print(solution.combinationSum2(candidates,target))