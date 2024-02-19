//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int minValue(string s, int k){
        // code here
        map<char,int> m;
        priority_queue<int> mp;
        for(int i = 0;i<s.size();i++){
            m[s[i]]++;
        }
        for(auto it:m){
            mp.push(it.second);
            
        }
        while(k>0){
            int ele = mp.top();
            mp.pop();
            ele = ele - 1;
            k = k-1;
            mp.push(ele);
            
        }
        int su =0;
        while(!mp.empty()){
            int p = mp.top();
            su+=p*p;
            mp.pop();
        }
        return su;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        string s;
        int k;
        cin>>s>>k;
        
        Solution ob;
        cout<<ob.minValue(s, k)<<"\n";
    }
    return 0;
}
// } Driver Code Ends