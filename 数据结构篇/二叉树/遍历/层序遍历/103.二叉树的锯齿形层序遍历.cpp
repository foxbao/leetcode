

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
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        queue<TreeNode*>que;
        if(root!=nullptr)
        {
            que.push(root);
        }

        vector<vector<int>>result;
        while(!que.empty())
        {
            int size=que.size();
            vector<int>vec;
            for(int i=0;i<size;i++)
            {
                TreeNode* node=que.front();
                que.pop();
                vec.push_back(node->val);
                if(node->left)
                {
                    que.push(node->left);
                }
                if(node->right)
                {
                    que.push(node->right);
                }
            }
            result.push_back(vec);
            
        }
        return result;
    }

private:
};

int main()
{
    TreeNode *root = buildTree();
    // printTree(root);
    Solution solution;
    vector<vector<int>>result = solution.levelOrder(root);
    for (auto &v : result)
    {
        for (auto &i : v)
        {
            cout << i << " ";
        }
        cout << endl;
    }
}