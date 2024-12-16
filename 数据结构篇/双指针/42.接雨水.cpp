

#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    /* data */
};

class Solution
{
public:
    int trap(vector<int> &height)
    {
        if(height.size()<=2)
        {
            return 0;
        }
        vector<int> maxLeft(height.size(),0);
        vector<int> maxRight(height.size(),0);
        int size=maxRight.size();

        maxLeft[0]=height[0];
        for(int i=1;i<size;i++)
        {
            maxLeft[i]=max(maxLeft[i-1],height[i]);
        }  
        maxLeft[size-1]=height[size-1];
        for(int i=size-2;i>=0;i--)
        {
            maxRight[i]=max(maxRight[i+1],height[i]);
        }

        int sum=0;
        for(int i=0;i<size;i++)
        {
            int count=min(maxLeft[i],maxRight[i])-height[i];
            if(count>0)
            {
                sum+=count;
            }
        }
        return sum;
    }
private:
};

int main()
{
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}; // 示例输入
    Solution solution;
    cout << "Water trapped: " << solution.trap(height) << endl;
    return 0;
}