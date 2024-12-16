

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
    void travelsal(TreeNode *cur, vector<int> &vec)
    {
        if (cur == NULL)
            return;
        vec.push_back(cur->val);
        travelsal(cur->left, vec);
        travelsal(cur->right, vec);
    }

    vector<int> preoderTraversal(TreeNode *root){
        vector<int> vec;
        travelsal(root,vec);
        return vec;
    }

private:
};

int main()
{
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    Solution solution;
    vector<int> vec=solution.preoderTraversal(root);
    for (auto i : vec)
    {
        std::cout << i << std::endl;
    }
}