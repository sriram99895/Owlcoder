//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    void bfs(int i ,int j,vector<vector<char>>&grid,vector<vector<int>>&vis){
        queue<pair<int,int>> q;
        q.push({i,j});
        vis[i][j] = 1;
        int n = grid.size();
        int m = grid[0].size();
        while(!q.empty()){
            int nr = q.front().first;
            int nc = q.front().second;
            q.pop();
            for(int delr = -1;delr<=1;delr++){
                for(int delc = -1;delc<=1;delc++){
                    int nir = nr+delr;
                    int cir = nc+delc;
                    if(nir>=0 && nir<n && cir>=0 && cir<m && grid[nir][cir]== '1'&& !vis[nir][cir]){
                        q.push({nir,cir});
                        vis[nir][cir] = 1;
                    }
                }
            }
        }
        
    }
    // Function to find the number of islands.
    int numIslands(vector<vector<char>>& grid) {
        // Code here
        int n = grid.size();
        int m = grid[0].size();
        int c = 0;
        vector<vector<int>>vis(n,vector<int>(m,0));
        for(int i =0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(!vis[i][j] && grid[i][j] == '1'){
                     c++;
                    bfs(i,j,grid,vis);
                }
            }
        }
        return c;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends