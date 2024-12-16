#include <vector>
#include <queue>
#include <iostream>
using namespace std;


void printBoard(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (const auto& cell : row) {
            cout << cell << " ";
        }
        cout << endl;
    }
}
class Solution
{
public:
    void  solve(vector<vector<char>> &board)
    {
        int n = board.size(), m = board[0].size(); 
        // 步骤一：
        // 从左侧边，和右侧边 向中间遍历
        for (int i = 0; i < n; i++) {
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][m - 1] == 'O') dfs(board, i, m - 1);
        }

        // 从上边和下边 向中间遍历
        for (int j = 0; j < m; j++) {
            if (board[0][j] == 'O') dfs(board, 0, j);
            if (board[n - 1][j] == 'O') dfs(board, n - 1, j);
        }

        // 步骤二：
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == 'A') board[i][j] = 'O';
            }
        }

    }

private:
    int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    void dfs(vector<vector<char>> &board, int row, int col)
    {
        board[row][col]='A';
        for(auto dir:dirs)
        {
            int nextRow=row+dir[0];
            int nextCol=col+dir[1];
            if(nextRow<0||nextRow>=board.size()||nextCol<0||nextCol>=board[0].size())
            {
                continue;
            }
            if(board[nextRow][nextCol]=='X'||board[nextRow][nextCol]=='A')
            {
                continue;
            }
            dfs(board,nextRow,nextCol);
        }
        return;

    }
};

int main()
{
    Solution solution;
    vector<vector<char>> board = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'}};
    printBoard(board);
    std::cout<<std::endl;
    
    solution.solve(board);
    printBoard(board);
    return -1;
}