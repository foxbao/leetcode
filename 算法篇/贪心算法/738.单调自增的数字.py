# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。

# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

 

# 示例 1:

# 输入: n = 10
# 输出: 9
# 示例 2:

# 输入: n = 1234
# 输出: 1234
# 示例 3:

# 输入: n = 332
# 输出: 299
 

# 提示:

# 0 <= n <= 109

class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        strNum=str(n)
        stackNum=[]
        for num in strNum:
            stackNum.append(int(num))
        
        flag=len(stackNum)
        for i in range(len(stackNum)-1,0,-1):
            if stackNum[i-1]>stackNum[i]:
                flag=i
                stackNum[i-1]-=1
        for i in range(flag,len(stackNum)):
            stackNum[i]=9
            
        result=""
        for num in stackNum:
            result+=str(num)
        return int(result)
                
solution=Solution()
n=332
print(solution.monotoneIncreasingDigits(n))