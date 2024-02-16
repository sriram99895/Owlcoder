//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    void Dfs(int node,vector<int> adj[],vector<int> &vis){
        vis[node] = 1;
        for(auto it:adj[node]){
            if(!vis[it]){
                Dfs(it,adj,vis);
            }
        }
    }
    int numProvinces(vector<vector<int>> adj, int v) {
        // code here
        vector<int>ad[v+1];
        for(int i =0;i<v;i++){
            for(int j = 0;j<v;j++){
                if(adj[i][j] == 1 ){
                    ad[i+1].push_back(j+1);
                    ad[j+1].push_back(i+1);
                }
            }
        
    }
        vector<int> vis(v+1,0) ;
        int c = 0;
        for(int i = 1;i<v+1;i++){
            if(vis[i]==0){
                c++;
                Dfs(i,ad,vis);
            }
        } 
    return c;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int V,x;
        cin>>V;
        
        vector<vector<int>> adj;
        
        for(int i=0; i<V; i++)
        {
            vector<int> temp;
            for(int j=0; j<V; j++)
            {
                cin>>x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }
        

        Solution ob;
        cout << ob.numProvinces(adj,V) << endl;
    }
    return 0;
}
// } Driver Code Ends