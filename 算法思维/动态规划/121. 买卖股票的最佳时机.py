class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        dp=[0,0]*len(prices)
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],-prices[0])
            dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0])
        return dp[-1][1]
        # cost=float('inf')
        # profit=0
        
        # for price in prices:
        #     cost=min(cost,price)
        #     profit=max(profit,price-cost)
            
        # return profit
        
        
solution=Solution()   
nums=[2,3,2]
print(solution.maxProfit(nums))
        
        