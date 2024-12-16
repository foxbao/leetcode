class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res=0
        self.isisland=0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    self.dfs(grid,row,col)
                self.res=max(self.res,self.isisland)
                self.isisland=0
        return self.res
                    
    def dfs(self,grid,i,j):
        grid[i][j]=0
        self.isisland+=1
        dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        
        for dir in dirs:
            nrow,ncol=i+dir[0],j+dir[1]
            if nrow>=0 and nrow<len(grid) and ncol>=0 and ncol<len(grid[0]) and grid[nrow][ncol]:
                self.dfs(grid,nrow,ncol)
        
        