#include <vector>
#include <iostream>
using namespace std;
class Solution{
    public:
    int fib(int N){
        if(N<=1) return N;
        vector<int> dp(N+1);
        dp[0]=0;
        dp[1]=1;
        for(int i=2;i<=N;i++){
            dp[i]=dp[i-1]+dp[i-2];

        }
        return dp[N];
    }
    private:
};


int main()
{
    Solution solution;
    int N=5;
    int result=solution.fib(N);
    std::cout<<result<<std::endl;
}