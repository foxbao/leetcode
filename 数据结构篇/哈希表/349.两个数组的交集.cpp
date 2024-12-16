#include <vector>
#include <iostream>
#include <unordered_set>
using namespace std;
class Solution
{
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2)
    {
        unordered_set<int> result_set;
        int hash[1005]={0};
        for(int num:nums1)
        {
            hash[num]=1;
        }

        for(int num:nums2){
            if (hash[num]==1)
            {
                result_set.insert(num);
            }
        }

        for (auto aaa:result_set)
        {
            int bbb=2;
            bbb++;
        }
        return vector<int>(result_set.begin(),result_set.end());
    }

private:
};

int main()
{
    vector<int> nums1={1,2,2,2};
    vector<int> nums2={2,2};
    Solution solution;
    vector<int>result=solution.intersection(nums1,nums2);
    return 0;
}