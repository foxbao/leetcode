class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            res=res^num
            
        return res
    
a=1
b=0
c=a^b

ttt=2