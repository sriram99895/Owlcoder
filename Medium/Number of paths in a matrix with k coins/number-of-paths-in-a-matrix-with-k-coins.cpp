//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:
    long long dp[101][101][101];
    long long fun(int i,int j,vector<vector<int>> &arr,int n,int k){
        if (i == n-1 and j == n-1){
            if (k-arr[i][j] == 0){
                return 1;
            }
            return 0;
        }
        if (i>n-1 or j>n-1 or k<0){
            return 0;
        }
        if (dp[i][j][k]!=-1)return dp[i][j][k];
       return dp[i][j][k] =  fun(i+1,j,arr,n,k-arr[i][j])+fun(i,j+1,arr,n,k-arr[i][j]);
        
        
    }
    
    long long numberOfPath(int n, int k, vector<vector<int>> &arr){
        memset(dp,-1,sizeof(dp));
        
        long long ans =fun(0,0,arr,n,k);
        return ans;
        
        
        // Code Here
    }
};

//{ Driver Code Starts.

int main()
{
    Solution obj;
    int i,j,k,l,m,n,t;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        vector<vector<int>> v(n, vector<int>(n, 0));
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                cin>>v[i][j];
        cout << obj.numberOfPath(n, k, v) << endl;
    }
}
// } Driver Code Ends