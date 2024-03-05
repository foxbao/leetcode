class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length=len(nums)
        
        dp=[0 for _ in range(length)]
        
        dp[0]=nums[0]
        
        max_value=nums[0]
        for i in range(1,length):
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]
            max_value=max(max_value,dp[i])
        return max_value
            

