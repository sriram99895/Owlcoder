//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution 
{
    public:
    //Function to find minimum time required to rot all oranges. 
    int orangesRotting(vector<vector<int>>& grid) {
        // Code here
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>>vis(n,vector<int>(m,0));
        int delr []={-1,0,1,0};
        int delc[] = {0,1,0,-1};
        queue<pair<pair<int ,int>,int>>q;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(grid[i][j] == 2){
                    q.push({{i,j},0});
                    vis[i][j] = 1;
                }
            }
        }
        int vt = 0;
        while(!q.empty()){
            auto it = q.front();
            int r = it.first.first;
            int c = it.first.second;
            int t = it.second;
            vt = max(vt,t);
            q.pop();
            for(int i = 0;i<4;i++){
                int nr = delr[i]+r;
                int nc = delc[i]+c;
                // int nt = t+1;
                if(nr<n && nr>=0 && nc<m&& nc>=0 && !vis[nr][nc] && grid[nr][nc] == 1){
                 q.push({{nr,nc},t+1});
                 grid[nr][nc] = 2;
                 vis[nr][nc] = 1;
                }
            }
        }
        // return vt;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(grid[i][j] == 1){
                    return -1;
                }
            }
        }
        return vt;
        
        
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>grid(n, vector<int>(m, -1));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin >> grid[i][j];
			}
		}
		Solution obj;
		int ans = obj.orangesRotting(grid);
		cout << ans << "\n";
	}
	return 0;
}
// } Driver Code Ends