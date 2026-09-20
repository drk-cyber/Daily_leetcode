#include<iostream>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(root==nullptr){
            return true;
        }
        return check(root->left,root->right);
    }
    bool check(TreeNode* p,TreeNode* q){
        if(p==nullptr&&q==nullptr){
            return true;
        }
        if(p==nullptr||q==nullptr){
            return false;
        }
        if(p->val!=q->val){
            return false;
        }
        return check(p->left,q->right)&&check(q->left,p->right);
    }
};