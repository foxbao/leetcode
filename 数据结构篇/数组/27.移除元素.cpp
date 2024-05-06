#include <iostream>
#include <vector>
using namespace std;
// class Solution {
// public:
//     int removeElement(vector<int>& nums, int val) {
//         int size = nums.size();
//         for (int i = 0; i < size; i++) {
//             if (nums[i] == val) { // 发现需要移除的元素，就将数组集体向前移动一位
//                 for (int j = i + 1; j < size; j++) {
//                     nums[j - 1] = nums[j];
//                 }
//                 i--; // 因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
//                 size--; // 此时数组的大小-1
//             }
//         }
//         return size;
//     }
// };

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size=nums.size();
        int slowIndex=0;
        for(int fastIndex=0;fastIndex<size;fastIndex++){
            if(nums[fastIndex]!=val)
            {
                nums[slowIndex++]=nums[fastIndex];
            }
        }
        return slowIndex;
    }
};

int main()
{
    Solution solution;
    std::vector<int> nums = {0,1,2,2,3,0,4,2};
    int val = 2;
    int size = solution.removeElement(nums, val);
    for(int i = 0; i < size; i++)
    {
        std::cout<<nums[i]<<std::endl;
    }
    return 0;
}