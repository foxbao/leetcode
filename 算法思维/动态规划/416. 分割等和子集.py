# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

# 示例 1：

# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 示例 2：

# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
 

# 提示：

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalSum=sum(nums)
        # target=totalSum/2

        dp=[0]*10001


        
        dp=[0]*(target_sum+1)
        for i in range(len(nums)):
            for j in range(target_sum,nums[i]-1,-1):
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
                
        if(dp[target_sum]==target_sum):
            return True
        return False
        # dp=[[False]*(target_sum+1) for _ in range(len(nums)+1)]
        
        # for i in range(len(nums)+1):
        #     dp[i][0]=True
        
        # for i in range(1,len(nums)+1):
        #     for j in range(1,target_sum+1):
        #         if j < nums[i-1]:
        #             dp[i][j]=dp[i-1][j]
        #         else:
        #             dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
        # return dp[len(nums)][target_sum]
        
        
solution=Solution()
nums=[1,5,11,5]
print(solution.canPartition(nums))