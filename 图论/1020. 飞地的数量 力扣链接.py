# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

 

# 示例 1：


# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
# 示例 2：


# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
 

# 提示：

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1

from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rowSize=len(grid)
        colSize=len(grid[0])
        self.result=0
        self.dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        self.visited=[[False]*colSize for _ in range(rowSize)]
        queue=deque()
        
        for row in range(rowSize):
            if grid[row][0]==1:
                self.visited[row][0]=True
                queue.append([row,0])
            if grid[row][colSize - 1] == 1:
                self.visited[row][colSize - 1] = True
                queue.append([row,colSize - 1])
                
        for col in range(1, colSize - 1):
            if grid[0][col] == 1:
                self.visited[0][col] = True
                queue.append([0, col])
            if grid[rowSize - 1][col] == 1:
                self.visited[rowSize - 1][col] = True
                queue.append([rowSize - 1, col])
        self.BSF(grid, queue)
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == 1 and not self.visited[row][col]:
                    self.result += 1
        return self.result
        
    def BSF(self,grid,queue):
        while queue:
            curPos=queue.popleft()
            for dir in self.dirs:
                newRow=curPos[0]+dir[0]
                newCol=curPos[1]+dir[1]
                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]): continue
                # 当前位置值不是 1 或者已经被访问过了
                if grid[newRow][newCol] == 0 or self.visited[newRow][newCol]: continue
                self.visited[newRow][newCol] = True
                queue.append([newRow,newCol])
        
    #     #DFS
    #     rowSize=len(grid)
    #     colSize=len(grid[0])
    #     self.result=0
    #     self.dirs=[[-1,0],[1,0],[0,-1],[0,1]]
    #     self.visited=[[False]*colSize for _ in range(rowSize)]
        
    #     for row in range(rowSize):
    #         if grid[row][0]==1:
    #             self.visited[row][0]=True
    #             self.DFS(row,0,grid)
    #         if grid[row][colSize-1]==1:
    #             self.visited[row][colSize-1]=True
    #             self.DFS(row,colSize-1,grid)
                
    #     for col in range(1, colSize - 1):
    #         if grid[0][col] == 1:
    #             self.visited[0][col] = True
    #             self.DFS(0, col,grid)
    #         if grid[rowSize - 1][col] == 1:
    #             self.visited[rowSize - 1][col] = True
    #             self.DFS(rowSize - 1, col,grid)

    #     for row in range(rowSize):
    #         for col in range(colSize):
    #             if grid[row][col]==1 and not self.visited[row][col]:
    #                 self.result+=1
    #     return self.result
                
    # def DFS(self,row,col,grid):
    #     for dir in self.dirs:
    #         newRow=row+dir[0]
    #         newCol=col+dir[1]
    #         if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
    #             continue
    #         if grid[newRow][newCol] == 0 or self.visited[newRow][newCol]: 
    #             continue
    #         self.visited[newRow][newCol] = True
    #         self.DFS(newRow,newCol,grid)
        
solution=Solution()
grid=[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(solution.numEnclaves(grid))