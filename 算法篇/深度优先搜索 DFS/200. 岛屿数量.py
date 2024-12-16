class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """        

        res=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1":
                    self.dfs(grid,row,col)
                    res += 1
        return res

    def dfs(self,grid,i,j):
        dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        grid[i][j]="0"
        for dir in dirs:
            nrow,ncol=i+dir[0],j+dir[1]
            if nrow>=0 and nrow<len(grid) and ncol>=0 and ncol<len(grid[0]):
                if grid[nrow][ncol]=="1":
                    self.dfs(grid,nrow,ncol)
        
solution=Solution()
grid=[["1","1"],["1","1"]]
res=solution.numIslands(grid) 
print(res)           
