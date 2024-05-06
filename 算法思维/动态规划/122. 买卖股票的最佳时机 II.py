class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        
        return dp[-1][1]
        
        # ans=0
        # for i in range(len(prices)-1):
        #     if prices[i+1]-prices[i]>0:
        #         ans+=prices[i+1]-prices[i]
        # return ans
        
solution=Solution()   
nums=[2,3,2]
print(solution.maxProfit(nums))
                