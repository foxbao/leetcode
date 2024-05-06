class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        totalSum=sum(stones)
        target=totalSum//2
        dp=[0]*15001
        
        for i in range(len(stones)):
            for j in range(target,stones[i]-1,-1):
                dp[j]=max(dp[j],dp[j-stones[i]]+stones[i])
        return totalSum-dp[target]-dp[target]
        
solution=Solution()
stones=[2,7,4,1,8,1]
print(solution.lastStoneWeightII(stones))