#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 二叉树节点定义
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 根据数组构造二叉树
TreeNode *buildTree(const vector<int> &nodes)
{
    if (nodes.empty())
        return nullptr;

    // 创建根节点
    TreeNode *root = new TreeNode(nodes[0]);
    queue<TreeNode *> q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < nodes.size())
    {
        TreeNode *curr = q.front();
        q.pop();

        // 构造左子节点
        if (nodes[i] != -1)
        { // -1 表示空节点
            curr->left = new TreeNode(nodes[i]);
            q.push(curr->left);
        }
        i++;

        // 构造右子节点
        if (i < nodes.size() && nodes[i] != -1)
        {
            curr->right = new TreeNode(nodes[i]);
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

// 层序遍历打印二叉树
void printTree(TreeNode *root)
{
    if (!root)
        return;

    queue<TreeNode *> q;
    q.push(root);
    while (!q.empty())
    {
        TreeNode *curr = q.front();
        q.pop();
        if (curr)
        {
            cout << curr->val << " ";
            q.push(curr->left);
            q.push(curr->right);
        }
        else
        {
            cout << "null ";
        }
    }
    cout << endl;
}

class Solution
{
public:
    int sumOfLeftLeaves(TreeNode *root)
    {
        if (root == NULL)
            return 0;
        if (root->left == NULL && root->right == NULL)
            return 0;

        int leftValue = sumOfLeftLeaves(root->left); // 左
        if (root->left && !root->left->left && !root->left->right)
        { // 左子树就是一个左叶子的情况
            leftValue = root->left->val;
        }
        int rightValue = sumOfLeftLeaves(root->right); // 右

        int sum = leftValue + rightValue; // 中
        return sum;
    }
};
// 测试翻转后的结果
int main()
{
    vector<int> nodes = {4, 2, 7, 1, 3, 6, 9};
    TreeNode *root = buildTree(nodes);

    cout << "原始二叉树（层序遍历）: ";
    printTree(root);

    // 在这里调用你的翻转二叉树函数，例如 invertTree(root);
    Solution solution;
    int sum = solution.sumOfLeftLeaves(root);

    return 0;
}
