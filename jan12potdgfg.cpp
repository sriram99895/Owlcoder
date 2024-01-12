#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
    
    // Function to reverse first k elements of a queue.
    queue<int> modifyQueue(queue<int> q, int k) {
        // add code here.
        queue<int> qq;
        stack<int> s;
        while(k--){
            int a = q.front();
            q.pop();
            s.push(a);
        }
        while(!s.empty()){
            int a = s.top();
            s.pop();
            qq.push(a);
            
        }
        while(!q.empty()){
            int a = q.front();
            qq.push(a);
            q.pop();
        }
        return qq;
    }
};
