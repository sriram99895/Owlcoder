bool cmp(pair<int,int>p1,pair<int,int>p2){
    return p1.first<p2.first;

}
class Solution {
public: 
    int fun(int n,vector<int>&mapping){
        int s = 0;
        int i = 0;
        if(n==0)return mapping[n];
        while(n>0){
            int r = n%10;
            s+=mapping[r]*pow(10,i);
            i+=1;
            n = n/10;

        }
        return s;
    }
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        // unordered_map<int,int>m;
       vector<pair<int,int>>arr;
        for(int i =0;i<nums.size();i++){
            int c = fun(nums[i],mapping);
            pair<int,int>m = make_pair(c,i);
            arr.push_back(m);
        }
        // cout<<fun(9,mapping);
        // for(auto it:arr){
        //     cout<<it.first<<" "<<it.second<<"\n";
        // }
        sort(arr.begin(),arr.end(),cmp);
        vector<int>result;
        for(auto it:arr){
            result.push_back(nums[it.second]);
        }
        return result;
        
    }
};