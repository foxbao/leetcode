# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

# 示例 1：


# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 示例 2：

# 输入：n = 1
# 输出：[[1]]
 

# 提示：

# 1 <= n <= 20

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        
        nums=[[0]*n for i in range(n)]
        #转n/2圈
        loop=n//2
        mid = n // 2
        offset=1
        startx=0
        starty=0
        count=1
        for offset in range(1, loop + 1):
            for j in range(starty,n-offset):
                nums[startx][j]=count
                count+=1
            for i in range(startx,n-offset):
                nums[i][n-offset]=count
                count+=1
            for j in range(n-offset,starty,-1):
                nums[n-offset][j]=count
                count+=1
            for i in range(n-offset,startx,-1):
                nums[i][starty]=count
                count+=1
            startx+=1
            starty+=1
            
        #如果n是奇数,n%2=1,最后一个中心值单独赋值
        if n%2==1:
            nums[mid][mid]=count
        return nums
solution=Solution()
target = 3
print(solution.generateMatrix(target))