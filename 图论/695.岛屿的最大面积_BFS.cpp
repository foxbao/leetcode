// # 已解答
// # 中等
// # 相关标签
// # 相关企业
// # 给你一个大小为 m x n 的二进制矩阵 grid 。

// # 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

// # 岛屿的面积是岛上值为 1 的单元格的数目。

// # 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

// # 示例 1：

// # 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
// # 输出：6
// # 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
// # 示例 2：

// # 输入：grid = [[0,0,0,0,0,0,0,0]]
// # 输出：0

// # 提示：

// # m == grid.length
// # n == grid[i].length
// # 1 <= m, n <= 50
// # grid[i][j] 为 0 或 1
#include <vector>
#include <queue>
using namespace std;
class Solution
{
public:
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited = vector<vector<bool>>(rows, vector<bool>(cols, false));
        int result = 0;
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if(!visited[i][j] && grid[i][j]==1){
                    count=0;
                    bfs(grid,visited,i,j);
                    result=max(result,count);
                }
            }
        }
        return result;
    }

private:
    int count;
    int dirs[4][2] = {-1, 0, 1, 0, 0, -1, 0, 1};
    void bfs(vector<vector<int>> &grid, vector<vector<bool>> &visited, int row, int col)
    {
        queue<pair<int, int>> que;
        que.push({row, col});
        visited[row][col] = true;
        count++;
        while (!que.empty())
        {
            pair<int,int> cur=que.front();
            que.pop();
                int curRow=cur.first;
                int curCol=cur.second;
            for(auto dir:dirs)
            {
                int nextRow=curRow+dir[0];
                int nextCol=curCol+dir[1];
                if (nextRow < 0 || nextRow >= grid.size() || nextCol < 0 || nextCol > grid[0].size())
                {
                    continue;
                }
                if (!visited[nextRow][nextCol] && grid[nextRow][nextCol] == '1')
                {
                    que.push({nextRow, nextCol});
                    visited[nextRow][nextCol] = true;
                    count++;
                }
            }
        }
    }
};

int main()
{
    Solution solution;
    // vector<int> nums={1,2,3,4,5};
    // solution.threeSum(nums);
    return 1;
}