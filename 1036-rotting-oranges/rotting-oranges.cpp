class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // int n = grid.size();
        // int m = grid[0].size();
        // queue<pair<pair<int,int>,int>>q;
        // int delr[] = {-1,0,1,0};
        // int delc[] = {0,1,0,-1};
        // // vector<vector<int>>vis(n,vector<int>v(m,0));
        // vector<vector<int>>vis(n,vector<int>(m,0));
        // for(int i = 0;i<n;i++){
        //     for(int j =0;i<m;j++){
        //         if(grid[i][j] == 2){
        //             q.push({{i,j},0});
        //             vis[i][j] = 1;
        //         }
        //     }
        // }
        // int ma = -1;
        // while(!q.empty()){
        //     auto it = q.front();
        //     int r = it.first.first;
        //     int c = it.first.second;
        //     int t = it.second;
        //     ma = max(ma,t);
        //     for(int i =0;i<4;i++){
        //         int nr = r+delr[i];
        //         int nc = c +delc[i];
        //         if(nr<n&& nc<m && nr>=0 && nc>=0 && grid[nr][nc] == 1 && !vis[nr][nc]){
        //          q.push({{nr,nc},t+1}); 
        //          vis[nr][nc] = 1; 
        //          grid[nr][nc] = 2; 
        //         }
        //     }
        // }
        // return ma;
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