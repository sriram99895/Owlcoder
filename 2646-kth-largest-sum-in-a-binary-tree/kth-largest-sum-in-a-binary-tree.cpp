/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        queue<TreeNode*> q;

        vector<long long> v;
        q.push(root);
        while(!q.empty()){
            int n = q.size();
            long long s = 0;
            for(int i =0;i<n;i++){
                TreeNode* k = q.front();
                q.pop();
                if(k->left!=NULL)q.push(k->left);
                if(k->right!=NULL)q.push(k->right);
                s+=k->val;
            }
            v.push_back(s);
        }
        int p = v.size();
        if(k>p)return -1;
        sort(v.rbegin(),v.rend());
        // for(int i =0;i<p;i++){
        //     cout << v[i]<< " ";
        // }
        return v[k-1];
        
    }
};