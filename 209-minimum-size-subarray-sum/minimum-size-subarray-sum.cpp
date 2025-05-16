class Solution {
public:
    int minSubArrayLen(int target, vector<int>& arr) {
        int n = arr.size();
        int start =0;
        int mine = 999999;
        int sum = 0;
        for(int end = 0;end<n;end++){
            sum+=arr[end];
            while(sum>=target && start<=end){
               mine = min(mine,(end-start+1));
               sum-=arr[start];
               start++;  
            }

        }
        if(mine == 999999){
            return 0;
        }
        return mine;
    }
};