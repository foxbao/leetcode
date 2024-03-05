class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cover=0
        if len(nums)==1:
            return True
        idx=0
        while idx<=cover:
            
            cover=max(cover,idx+nums[idx])
            if cover>=len(nums)-1:
                return True
            idx+=1
        return False

solution=Solution()
nums=[2,3,1,1,4]
print(solution.canJump(nums))