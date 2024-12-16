

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

TreeNode *buildTree()
{
    TreeNode *root = new TreeNode(3);           // 根节点 3
    root->left = new TreeNode(5);               // 左子节点 5
    root->right = new TreeNode(1);              // 右子节点 1
    root->left->left = new TreeNode(6);         // 节点 5 的左子节点 6
    root->left->right = new TreeNode(2);        // 节点 5 的右子节点 2
    root->right->left = new TreeNode(0);        // 节点 1 的左子节点 0
    root->right->right = new TreeNode(8);       // 节点 1 的右子节点 8
    root->left->right->left = new TreeNode(7);  // 节点 2 的左子节点 7
    root->left->right->right = new TreeNode(4); // 节点 2 的右子节点 4
    return root;
}
void printTree(TreeNode *root)
{
    if (root == nullptr)
        return;
    cout << root->val << " ";
    printTree(root->left);
    printTree(root->right);
}

class Solution
{
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        if(root==q||root==p||root==nullptr)
        {
            return root;
        }
        TreeNode* left=lowestCommonAncestor(root->left,p,q);
        TreeNode* right=lowestCommonAncestor(root->right,p,q);
        if(left!=nullptr && right!=nullptr)
        {
            return root;
        }
        if(left==nullptr && right!=nullptr)
        {
            return right;
        }
        else if (left != nullptr && right == nullptr)
        {
            return left;
        }
        else
        {
            return nullptr;
        }

    }

private:
};

int main()
{
    TreeNode *root = buildTree();
    TreeNode *p = root->left->left;  // 节点 5
    TreeNode *q = root->left->right; // 节点 1
    // printTree(root);
    Solution solution;
    TreeNode *result = solution.lowestCommonAncestor(root, p, q);
    std::cout << result->val << std::endl;
}