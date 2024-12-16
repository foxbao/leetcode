#include <vector>
#include <iostream>
using namespace std;
class Solution{
    public:
    int minCostClimbingStairs(vector<int>& cost){
        int n=cost.size();
        vector<int> dp(n+1,0);
        for(int i=2;i<=n;i++){
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-1]+cost[i-2]);
        }
        return dp[n];
    }
    private:
};


int main()
{
    Solution solution;
    vector<int> cost={10,15,20};
    int result=solution.minCostClimbingStairs(cost);
    std::cout<<result<<std::endl;
}