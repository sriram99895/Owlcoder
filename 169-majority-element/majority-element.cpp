class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int can = -1;
        int vote = 0;
        for(int i = 0;i<nums.size();i++){
            if(vote == 0){
                vote = 1;
                can = nums[i];
            }
            else{
                if(nums[i] == can){
                    vote++;
                }
                else{
                    vote--;
                }
            }
        }
        int c = 0;
        for(int i = 0;i<nums.size();i++){
            if(nums[i] == can){
                c++;
            }

    }
        if(c>int(nums.size())/2){
            return can;
        }
        return -1;
    }
};