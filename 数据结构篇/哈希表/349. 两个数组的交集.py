# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

 

# 示例 1：

# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 示例 2：

# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
 

# 提示：

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # 用数组
        hash=[0]*1005
        res=set()
        for num in nums1:
            hash[num]+=1
        for num in nums2:
            if hash[num]!=0:
                res.add(num)
        return list(res)
        
        
        # 用哈希
        # table=dict()
        # for num in nums1:
        #     table[num]=table.get(num,0)+1
            
        # res=set()
        # for num in nums2:
        #     if num in table:
        #         res.add(num)
        
        # return list(res)
        
        
solution=Solution()
nums1 = [4,9,5]
nums2=[9,4,9,8,4]
print(solution.intersection(nums1,nums2))