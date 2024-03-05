# 已解答
# 中等
# 相关标签
# 相关企业
# 给你一个大小为 m x n 的二进制矩阵 grid 。

# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

# 岛屿的面积是岛上值为 1 的单元格的数目。

# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

 

# 示例 1：


# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
# 示例 2：

# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
 

# 提示：

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] 为 0 或 1

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        self.dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        self.height=len(grid)
        self.width=len(grid[0])
        self.visited=[[False]*self.width for _ in range(self.height)]
        self.result=0
        self.count=0
        self.grid=grid
        for i in range(self.height):
            for j in range(self.width):
                if not self.visited[i][j] and self.grid[i][j]==1:
                    self.count=1
                    self.visited[i][j]=True
                    self.DFS(i,j)
                    self.result=max(self.result,self.count)
        return self.result

    def DFS(self,x,y):
        for dir in self.dirs:
            nextx=x+dir[0]
            nexty=y+dir[1]
            if nextx<0 or nextx>=self.height or nexty<0 or nexty >=self.width:
                continue
                
            if not self.visited[nextx][nexty] and self.grid[nextx][nexty]==1:
                self.visited[nextx][nexty]=True
                self.count+=1
                self.DFS(nextx,nexty)
        

solution=Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(solution.maxAreaOfIsland(grid))