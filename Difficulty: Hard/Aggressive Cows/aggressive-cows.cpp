//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
public:
    
    bool check(vector<int>&stalls,int n,int k,int p){
        int c = 1;
        int last = stalls[0];
        for(int i =1;i<n;i++){
            if(stalls[i]-last>=p){
                c++;
                last = stalls[i];
                if(c>=k){
                    return 1;
                }
            }
        }
        return 0;
    }
    int solve(int n, int k, vector<int> &stalls) {
    
        // Write your code here
        sort(stalls.begin(),stalls.end());
        int l = 1,h = stalls[n-1]-stalls[0];
        while(l<=h){
            int m = (l+h)/2;
            if(check(stalls,n,k,m)){
                l = m+1;
            }
            else{
                h = m-1;
            }
        }
        return h;
    }
};

//{ Driver Code Starts.

int main() {
    int t = 1;
    cin >> t;

    // freopen ("output_gfg.txt", "w", stdout);

    while (t--) {
        // Input

        int n, k;
        cin >> n >> k;

        vector<int> stalls(n);
        for (int i = 0; i < n; i++) {
            cin >> stalls[i];
        }
        // char ch;
        // cin >> ch;

        Solution obj;
        cout << obj.solve(n, k, stalls) << endl;

        // cout << "~\n";
    }
    // fclose(stdout);

    return 0;
}
// } Driver Code Ends