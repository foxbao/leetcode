#include <vector>
using namespace std;
class Solution
{
    public:
        int numIsLands(vector<vector<char>>&grid)
        {
            int n=grid.size();
            int m=grid[0].size();
            vector<vector<bool>>visited=vector<vector<bool>>(n,vector<bool>(m,false));
            int result=0;
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    if (!visited[i][j]&& grid[i][j]=='1')
                    {
                        visited[i][j]=true;
                        dfs(grid,visited,i,j);
                    }
                }
            }
        }
    private:
        int dirs[4][2]={0,1,0,-1,1,0,-1,0};
        void dfs(vector<vector<char>>& grid,vector<vector<bool>>& visited,int x, int y){
            for(int i=0;i<4;i++)
            {
                int nextx=x+dirs[i][0];
                int nexty=y+dirs[i][1];
                if(nextx<0 ||nextx>=grid.size()||nexty<0||nexty>=grid[0].size()){continue;}
                
            }
    }
};