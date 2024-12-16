# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 

# 示例 1：


# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 示例 2：

# 输入：board = [["X"]]
# 输出：[["X"]]
 

# 提示：

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.dirs=[[-1,0],[1,0],[0,1],[0,-1]]
        rows=len(board)
        cols=len(board[0])
        self.visited=[[False]*cols for _ in range(rows)]
        for j in range(cols):
            if board[0][j]=="O" and not self.visited[0][j]:
                self.dfs(board,0,j) 
            if board[rows-1][j] == "O" and not self.visited[rows-1][j]:
                self.dfs(board, rows-1, j)
        # 第一列和最后一列
        for i in range(1, rows-1):
            if board[i][0] == "O" and not self.visited[i][0]:
                self.dfs(board, i, 0, self.visited)
            if board[i][-1] == "O" and not self.visited[i][cols-1]:
                self.dfs(board, i, cols-1, self.visited)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
        
        
    def dfs(self,board,x,y):
        if self.visited[x][y] or board[x][y] == "X":
            return
        self.visited[x][y] = True
        board[x][y] = "A"
        for i in range(4):
            new_x = x + self.dirs[i][0]
            new_y = y + self.dirs[i][1]
            if new_x >= len(board) or new_y >= len(board[0]) or new_x < 0 or new_y < 0:
                continue
            self.dfs(board, new_x, new_y)
        
solution=Solution()
board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solution.solve(board))