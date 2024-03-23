/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode *cur = head;
        ListNode *ncu = head;
        vector<int> n;
        vector<int> v;
        int i = 0; 
        while(cur){
            v.push_back(cur->val);
            cur = cur->next;    
        }
        int j = v.size()-1;
        while(i<=j){
            if(i == j){
                n.push_back(v[i]);
                break;
            }
            n.push_back(v[i]);
            n.push_back(v[j]);
            i+=1;
            j-=1;

        }
        int k = 0;
        while(ncu){
            ncu->val = n[k];
            k++;
            ncu = ncu->next;
        }

    }
};