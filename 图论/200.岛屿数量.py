# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

 

# 示例 1：

# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
# 示例 2：

# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
 

# 提示：

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        self.height=len(grid)
        self.width=len(grid[0])
        self.visited=[[False]*self.width for _ in range(self.height)]
        self.result=0
        self.grid=grid
        for i in range(self.height):
            for j in range(self.width):
                if not self.visited[i][j] and self.grid[i][j]=='1':
                    self.visited[i][j]=True
                    self.result+=1
                    self.bfs(i,j)
        return self.result
        
        
    def bfs(self,i,j):
        que=deque()
        que.append((i,j))
        self.visited[i][j]=True
        while que:
            x,y=que.popleft()
            for dir in self.dirs:
                next_i=x+dir[0]
                next_j=y+dir[1]
                if next_i < 0 or next_i >= len(self.grid):
                    continue 
                if next_j < 0 or next_j >= len(self.grid[0]):
                    continue
                if self.visited[next_i][next_j]:
                    continue
                if self.grid[next_i][next_j] == '0':
                    continue
                que.append((next_i,next_j))
                self.visited[next_i][next_j]=True
        
    #     self.dirs=[[-1,0],[1,0],[0,-1],[0,1]]
    #     self.height=len(grid)
    #     self.width=len(grid[0])
    #     self.visited=[[False]*self.width for _ in range(self.height)]
    #     self.result=0
    #     self.grid=grid
    #     for i in range(self.height):
    #         for j in range(self.width):
    #             if not self.visited[i][j] and self.grid[i][j]=='1':
    #                 self.result+=1
    #                 self.dfs(i,j)
    #     return self.result

    # def dfs(self,i,j):
    #     if self.visited[i][j]:
    #         return
    #     self.visited[i][j]=True
    #     for dir in self.dirs:
    #         next_i=i+dir[0]
    #         next_j=j+dir[1]
    #         if next_i < 0 or next_i >= len(self.grid):
    #             continue 
    #         if next_j < 0 or next_j >= len(self.grid[0]):
    #             continue
    #         if self.visited[next_i][next_j]:
    #             continue
    #         if self.grid[next_i][next_j] == '0':
    #             continue
    #         self.dfs(next_i,next_j)
                
        
        
solution=Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(solution.numIslands(grid))