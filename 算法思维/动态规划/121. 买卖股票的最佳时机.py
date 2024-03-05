class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        cost=float('inf')
        profit=0
        
        for price in prices:
            cost=min(cost,price)
            profit=max(profit,price-cost)
            
        return profit
        
        
        