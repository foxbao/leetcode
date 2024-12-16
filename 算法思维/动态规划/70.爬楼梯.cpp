#include <vector>
#include <iostream>
using namespace std;
class Solution{
    public:
    int climbStairs(int N){
        if(N<=1) return N;
        vector<int> dp(N+1);
        dp[1]=1;
        dp[2]=2;
        for(int i=3;i<=N;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }
        return dp[N];
    }
    private:
};


int main()
{
    Solution solution;
    int N=8;
    int result=solution.climbStairs(N);
    std::cout<<result<<std::endl;
}