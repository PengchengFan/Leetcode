/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        if(!root){
            return 0;
        }
        int l = rangeSumBST(root->left, L, R);
        int r = rangeSumBST(root->right, L, R);
        if(root->val >=L && root->val <= R){
            return l + r + root->val;
        }
        return l + r;
    }
};