# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
# 如果气温在这之后都不会升高，请在该位置用 0 来代替。

# 示例 1:

# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 示例 2:

# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
# 示例 3:

# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
 

# 提示：

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        
        stack=list()
        stack.append(0)
        ans=[0 for i in range(len(temperatures))]
        for i in range(1,len(temperatures)):
            if temperatures[i]<temperatures[stack[-1]]:
                stack.append(i)
            elif temperatures[i]==temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and temperatures[i]>temperatures[stack[-1]]:
                    ans[stack[-1]]=i-stack[-1] 
                    stack.pop()
                stack.append(i)
        return ans
                    
                
        # ans=[0 for i in range(len(temperatures))]
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             ans[i]=j-i
        #             break
        return ans
        
solution=Solution()
temperatures=[73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures))