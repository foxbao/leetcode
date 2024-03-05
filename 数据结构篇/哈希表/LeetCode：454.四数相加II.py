# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

# 示例 1：

# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
# 示例 2：

# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1
 

#   提示：

# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        res=0
        hash_table=dict()
        for num1 in nums1:
            for num2 in nums2:
                sum=num1+num2
                hash_table[sum]=hash_table.get(sum,0)+1
        
        for num3 in nums3:
            for num4 in nums4:
                sum=num3+num4
                if -sum in hash_table:
                    res+=hash_table[-sum]
        
        return res
        
solution=Solution()
nums1 = [1,2]
nums2= [-2,-1]
nums3= [-1,2]
nums4= [0,2]
print(solution.twoSum(nums1, nums2, nums3, nums4))