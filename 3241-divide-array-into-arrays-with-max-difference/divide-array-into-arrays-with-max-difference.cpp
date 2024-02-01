class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> v;
        for(int i =0;i<nums.size();i+=3){
            vector<int> nw;
            for(int j = i;j<i+3;j++){
                nw.push_back(nums[j]);
            }
            v.push_back(nw);
        }
        for(auto it:v){
            if (abs(it[0]-it[2])>k){
                return {};
            }
        }
        return v;

        
    }
};