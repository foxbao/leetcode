

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
    int getdepth(TreeNode *node)
    {
        if (node==nullptr)
        {
            return 0;
        }
        int leftdepth=getdepth(node->left);
        int rightdepth=getdepth(node->right);
        int depth=1+max(leftdepth,rightdepth);
        return depth;
    }

    int maxDepth(TreeNode *root){
        return getdepth(root);
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
    int depth=solution.maxDepth(root);
    std::cout<<depth<<std::endl;
}