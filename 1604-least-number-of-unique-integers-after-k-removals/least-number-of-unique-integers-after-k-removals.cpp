 bool cmp(pair<int,int>&p,pair<int,int>&q){
        return p.second<q.second;
    }
class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        for(int i = 0;i<nums.size();i++){
           m[nums[i]]++;
        }

        vector<pair<int,int>> v;
        for(auto it:m){
            v.push_back(make_pair(it.first,it.second));
        }

        sort(v.begin(),v.end(),cmp);

        int c = 0;
        for(auto it:v){
            if(it.second<=k){
                c++;
                k = k-it.second;
            }
            else{
                break;
            }
        }
        int p = v.size()-c;
        // for(auto it:v){
        //     cout << it.first<<it.second<<endl;
        // }
        return p;
        // int c = 0;
        // for(auto it:v){
        //     if(it.second>0){
        //         c++;
        //     }
        // }
        // return c;
        
    }
};