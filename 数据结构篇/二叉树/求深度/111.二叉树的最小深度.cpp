

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
        if (node == nullptr)
        {
            return 0;
        }

        int leftDepth = getdepth(node->left);
        int rightDepth = getdepth(node->right);
        // 当一个左子树为空，右不为空，这时并不是最低点
        if (node->left == NULL && node->right != NULL)
        {
            return 1 + rightDepth;
        }
        // 当一个右子树为空，左不为空，这时并不是最低点
        if (node->left != NULL && node->right == NULL)
        {
            return 1 + leftDepth;
        }
        int depth = 1 + min(leftDepth, rightDepth);
        return depth;
    }

    int minDepth(TreeNode *root)
    {
        return getdepth(root);
    }

private:
};

TreeNode* buildTree() {
    TreeNode* root = new TreeNode(3); // 根节点 3
    root->left = new TreeNode(9);     // 左子节点 9
    root->right = new TreeNode(20);   // 右子节点 20
    root->right->left = new TreeNode(15); // 节点 20 的左子节点 15
    root->right->right = new TreeNode(7); // 节点 20 的右子节点 7
    return root;
}

void printTree(TreeNode* root) {
    if (root == nullptr) return;
    cout << root->val << " ";
    printTree(root->left);
    printTree(root->right);
}

int main()
{
    TreeNode* root = buildTree();
    printTree(root);
    Solution solution;
    int depth = solution.minDepth(root);
    std::cout << depth << std::endl;
}