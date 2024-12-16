

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
    TreeNode *root = new TreeNode(3);     // 根节点 3
    root->left = new TreeNode(9);         // 左子节点 9
    root->right = new TreeNode(20);       // 右子节点 20
    root->right->left = new TreeNode(15); // 节点 20 的左子节点 15
    root->right->right = new TreeNode(7); // 节点 20 的右子节点 7
    return root;
}

class Solution {
private:
    bool traversal(TreeNode* cur, int count) {
        if (!cur->left && !cur->right && count == 0) return true; // 遇到叶子节点，并且计数为0
        if (!cur->left && !cur->right) return false; // 遇到叶子节点直接返回

        if (cur->left) { // 左
            count -= cur->left->val; // 递归，处理节点;
            if (traversal(cur->left, count)) return true;
            count += cur->left->val; // 回溯，撤销处理结果
        }
        if (cur->right) { // 右
            count -= cur->right->val; // 递归，处理节点;
            if (traversal(cur->right, count)) return true;
            count += cur->right->val; // 回溯，撤销处理结果
        }
        return false;
    }

public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL) return false;
        return traversal(root, sum - root->val);
    }
};

int main()
{
    TreeNode *root = buildTree();

    Solution solution;
    int sum=12;
    bool has_path = solution.hasPathSum(root,sum);
    std::cout << has_path << std::endl;
}