#include <vector>
#include <queue>
using namespace std;
class Solution
{
public:
    int numIsLands(vector<vector<char>> &grid)
    {
        int rows = grid.size();
        int cols = grid[0].size();
        int result = 0;
        vector<vector<bool>> visited = vector<vector<bool>>(rows, vector<bool>(cols, false));
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if(!visited[i][j]&&grid[i][j]=='1'){
                    result++;
                    bfs(grid,visited,i,j);
                }
            }
        }
        return 1;
    }

private:
    int dirs[4][2] = {-1, 0, 1, 0, 0, -1, 0, 1};
    void bfs(vector<vector<char>> &grid, vector<vector<bool>> &visited, int row, int col)
    {
        queue<pair<int, int>> que;
        que.push({row, col});
        visited[row][col] = true;
        while (!que.empty())
        {
            pair<int, int> cur = que.front();
            que.pop();
            int curRow = cur.first;
            int curCol = cur.second;
            for (auto dir : dirs)
            {
                int nextRow = curRow + dir[0];
                int nextCol = curCol + dir[1];
                if (nextRow < 0 || nextRow >= grid.size() || nextCol < 0 || nextCol > grid[0].size())
                {
                    continue;
                }
                if (!visited[nextRow][nextCol] && grid[nextRow][nextCol] == '1')
                {
                    que.push({nextRow, nextCol});
                    visited[nextRow][nextCol] = true;
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