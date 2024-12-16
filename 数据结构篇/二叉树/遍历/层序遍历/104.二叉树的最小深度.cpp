

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
    int minDepth(TreeNode *root)
    {
        if(root==nullptr)
        {
            return 0;
        }
        int depth=0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            int size=q.size();
            depth++;
            for(int i=0;i<size;i++)
            {
                TreeNode* node=q.front();
                q.pop();
                if(node->left!=nullptr){
                    q.push(node->left);
                }
                if(node->right!=nullptr){
                    q.push(node->right);
                }
                if(!node->left && !node->right){
                    return depth;
                }
            }
        }
        return depth;
    }

private:
};

int main()
{
    TreeNode *root = buildTree();
    // printTree(root);
    Solution solution;
    int depth = solution.minDepth(root);
    std::cout<<depth<<std::endl;
}