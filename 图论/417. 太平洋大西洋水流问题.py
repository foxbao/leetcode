class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows=len(heights)
        cols=len(heights[0])
        self.result=[]
        self.visited=[[[False for _ in range(2)] for _ in range(cols)] for _ in range(rows)]
        self.dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        for row in range(rows):
            self.visited[row][0][1] = True
            self.visited[row][cols - 1][0] = True
            self.dfs(heights, row, 0, 1,)
            self.dfs(heights, row, cols - 1, 0)
        for col in range(0, cols):
            self.visited[0][col][1] = True
            self.visited[rows - 1][col][0] = True
            self.dfs(heights, 0, col, 1)
            self.dfs(heights, rows - 1, col, 0)
        for row in range(rows):
            for col in range(cols):
                # 如果该位置即可以到太平洋又可以到大西洋，就放入答案数组
                if self.visited[row][col][0] and self.visited[row][col][1]:
                    self.result.append([row, col])
        return self.result
        
        
    def dfs(self,heights,row,col,sign):
        for dir in self.dirs:
            newRow=row+dir[0]
            newCol=col+dir[1]
            if newRow < 0 or newRow >= len(heights) or newCol < 0 or newCol >= len(heights[0]): 
                continue
            if heights[newRow][newCol] < heights[row][col] or self.visited[newRow][newCol][sign]:
                continue
            self.visited[newRow][newCol][sign] = True
            self.dfs(heights, newRow, newCol, sign)
                
        
solution=Solution()
heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(solution.pacificAtlantic(heights))