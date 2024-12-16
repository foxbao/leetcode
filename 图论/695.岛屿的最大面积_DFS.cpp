#include <vector>
#include <queue>
using namespace std;
class Solution
{
public:
    int maxAreaOfIsland(vector<vector<char>> &grid){
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
                    count=1;
                    visited[i][j]=true;
                    dfs(grid,visited,i,j);
                    result=max(result,count);
                }
            }
        }
        return result;
    }

private:
    int dirs[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
    int count;
    void dfs(vector<vector<char>> &grid,vector<vector<bool>>&visited,int row,int col)
    {
        for(auto dir:dirs){
            int nextRow=row+dir[0];
            int nextCol=col+dir[1];
            if(nextRow<0||nextRow>=grid.size()||nextCol<0||nextCol>=grid[0].size())
            {
                continue;
            }
            if(!visited[nextRow][nextCol]&&grid[nextRow][nextCol]=='1')
            {
                count++;
                visited[nextRow][nextCol]=true;
                dfs(grid,visited,nextRow,nextCol);
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
    int result=solution.maxAreaOfIsland(grid);
    return -1;
}