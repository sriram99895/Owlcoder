class Solution {
public:
    void dfs(int node,vector<int>adj[],vector<int>&vis){
        vis[node] = 1;
        for(auto it:adj[node]){
            if(!vis[it]){
                dfs(it,adj,vis);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& add) {
    int n = add.size();
    vector<int>adj[n+1];
    for(int i = 0 ;i<n;i++){
        for(int j = 0;j<n;j++){
            if(add[i][j] == 1){
                adj[i+1].push_back(j+1);
                adj[j+1].push_back(i+1);
            }
        }
    }
    int c = 0;
    vector<int>vis(n+1,0);
    for(int i = 1;i<n+1;i++){
        if(!vis[i]){
            c++;
            dfs(i,adj,vis);
        }
    }
    return c;
        
    }
};