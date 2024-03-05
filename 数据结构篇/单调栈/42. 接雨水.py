# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 示例 2：

# 输入：height = [4,2,0,3,2,5]
# 输出：9
 

# 提示：

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        stack=list()
        stack.append(0)
        
        for i in range(1,len(height)):
            if height[i]<stack[-1]:
                stack.append(i)
            elif height[i]==stack[-1]:
                stack.append(i)
            else:
                pass
                
        #双指针
        # sum=0
        # maxLeft=[0 for i in range(len(height))]
        # maxRight=[0 for i in range(len(height))]
        
        # size=len(height)
        # maxLeft[0]=height[0]
        # for i in range(1,len(height)):
        #     maxLeft[i]=max(maxLeft[i-1],height[i])
            
        # maxRight[size-1]=height[size-1]
        
        # for i in range(size-2,-1,-1):
        #     maxRight[i]=max(maxRight[i+1],height[i])
            
        # for i in range(size):
        #     count=min(maxLeft[i],maxRight[i])-height[i]
        #     if count>0:
        #         sum=sum+count
                
        # return sum
        
solution=Solution()
height=[4,2,0,3,2,5]
print(solution.trap(height))

