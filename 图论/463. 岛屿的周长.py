# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

# 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

 

# 示例 1：



# 输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# 输出：16
# 解释：它的周长是上面图片中的 16 个黄色的边
# 示例 2：

# 输入：grid = [[1]]
# 输出：4
# 示例 3：

# 输入：grid = [[1,0]]
# 输出：4
 

# 提示：

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] 为 0 或 1

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        result=0
        rows=len(grid)
        cols=len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    for dir in dirs:
                        new_row=row+dir[0]
                        new_col=col+dir[1]
                        if new_row<0 or new_row>=rows or new_col<0 or new_col>=cols or grid[new_row][new_col]==0:
                            result+=1
        return result
        
        
        
        
solution=Solution()
grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(solution.islandPerimeter(grid))