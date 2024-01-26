//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

bool cmp(pair<int,int>a,pair<int,int>b){
    if(a.second == b.second){
        return a.first>b.first;
    }
    return a.second>b.second;
}
class Solution {
  public:
    vector<int> topK(vector<int>& nums, int k) {
        // Code here
    unordered_map<int,int> m;
    for(int i = 0;i<nums.size();i++){
        m[nums[i]]++;

    }
    vector<pair<int,int>> v;
    for(auto it:m){
       pair<int,int>k = {it.first,it.second};
       v.push_back(k);
    } 
    sort(v.begin(),v.end(),cmp);
    vector <int> nw;
    
    for(int i =0;i<k;i++){
    nw.push_back(v[i].first);
    }
    return nw;
    }
};


//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n;
        cin >> n;
        vector<int> nums(n);
        for (auto &i : nums) cin >> i;
        int k;
        cin >> k;
        Solution obj;
        vector<int> ans = obj.topK(nums, k);
        for (auto i : ans) cout << i << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends