#include <vector>
#include <queue>
using namespace std;
class Solution
{
public:
    int numIsLands(vector<vector<char>> &grid){
        int m=grid.size();
        int n=grid[0].size();
        int result = 0;
        vector<vector<bool>> visited(m,vector<bool>(n,false));
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(!visited[i][j]&&grid[i][j]=='1')
                {
                    result++;
                    bfs(grid,visited,i,j);
                }
            }
        }
        return result;
    }

private:
    int dirs[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
    void bfs(vector<vector<char>> &grid,vector<vector<bool>>&visited,int row,int col)
    {
        queue<pair<int,int>> q;
        q.push({row,col});
        visited[row][col]=true;
        while (!q.empty())
        {
            pair<int, int> cur = q.front();
            q.pop();
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
                    q.push({nextRow, nextCol});
                    visited[nextRow][nextCol] = true;
                }
            }
        }
    }
};

int main()
{
    Solution solution;
    std::vector<std::vector<char>> grid={{'1','1','1','1','0'},
    {'1','1','0','1','0'},
    {'1','1','0','0','0'},
    {'0','0','0','0','0'}};
    int result=solution.numIsLands(grid);
    return -1;
}