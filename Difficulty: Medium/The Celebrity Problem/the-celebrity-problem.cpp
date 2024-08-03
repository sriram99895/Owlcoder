//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:

    // Function to find if there is a celebrity in the party or not.
    int celebrity(vector<vector<int> >& mat) {
        // code here
        int n = mat[0].size();
        for(int i =0;i<mat[0].size();i++){
            int c = 0;
            int r = 0;
            for(int j =0;j<mat[0].size();j++){
                r+=mat[i][j];
                c+=mat[j][i];
            }
            if(r == 0 &&(c == n-1 || c == n)){
                return i;
            }
        }
        return -1;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int> > M(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> M[i][j];
            }
        }
        Solution ob;
        cout << ob.celebrity(M) << endl;
    }
}

// } Driver Code Ends