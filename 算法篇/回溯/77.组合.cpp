#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    vector<vector<int>> combination(int n,int k)
    {
        result.clear();
        path.clear();
        backtracking(n,k,1);
        return result;

    }

private:
    vector<vector<int>> result;
    vector<int>path;
    void backtracking(int n,int k,int startIndex)
    {
        if(path.size()==k)
        {
            result.push_back(path);
            return;
        }
        for(int i=startIndex;i<=n;i++)
        {
            path.push_back(i);
            backtracking(n,k,i+1);
            path.pop_back();
        }
    }
};

int main()
{
    int n=4;
    int k=2;
    Solution solution;
    vector<vector<int>> result=solution.combination(n,k);
    for(int i=0;i<result.size();i++)
    {
        for(int j=0;j<result[i].size();j++)
        {
            cout<<result[i][j]<<" ";
        }
        cout<<endl;
    }

}