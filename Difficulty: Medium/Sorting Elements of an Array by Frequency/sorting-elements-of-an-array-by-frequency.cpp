//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

bool cmp(pair<int,int>p,pair<int,int>q){
    if(p.second == q.second){
        return p.first<q.first;
    }
    return p.second>q.second;
}
class Solution {
  public:
    // Complete this function
    // Function to sort the array according to frequency of elements.
    vector<int> sortByFreq(vector<int>& arr) {
        // Your code here
        unordered_map<int,int> m;
        int n = arr.size();
        for(int i = 0;i<n;i++){
            m[arr[i]]++;
        }
        vector<pair<int,int>> v;
        for(auto it: m){
            v.push_back(it);
        }
        // for(auto it:v){
        //     cout  << it.first<<" "<< it.second;
        // }
        // cout << endl;
        sort(v.begin(),v.end(),cmp);
        // for(auto it:v){
        //     cout << it.first<< it.second;
        // }
        vector<int> nw;
        for(auto it:v){
            for(auto i = 0;i<it.second;i++){
                nw.push_back(it.first);
            }
            
        }
        return nw;
        
    }
};

//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    cin.ignore();
    while (t--) {

        string input;
        int num;
        vector<int> arr;

        getline(cin, input);
        stringstream s2(input);
        while (s2 >> num) {
            arr.push_back(num);
        }
        Solution obj;
        vector<int> v;
        v = obj.sortByFreq(arr);
        for (int i : v)
            cout << i << " ";
        cout << endl;
    }

    return 0;
}

// } Driver Code Ends