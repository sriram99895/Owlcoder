class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        long long s = 0;
        vector<long long> v;
        sort(nums.begin(),nums.end());
        for(int i = 0;i<nums.size();i++){
              s+=nums[i];
              v.push_back(s);
        }
        long long maxi = -1;
        for(int i =2;i<v.size();i++){
            if(nums[i]<v[i-1]){
                maxi = v[i];
            }
            else{
                continue;
            }

        }
        return maxi;

         
    }
};