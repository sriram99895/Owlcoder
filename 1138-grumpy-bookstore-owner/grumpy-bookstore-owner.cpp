class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
       int s = 0;
       for(int i = 0;i<grumpy.size();i++){
        if(grumpy[i] == 0){
            s+=customers[i];
        }
       }
       int m = 0;

       for(int i =0;i<grumpy.size()-minutes+1;i++){
        int k = 0;
        for(int j =0;j<minutes;j++){
            if(grumpy[i+j] == 1){
                // cout << customers[i+j];
                k+=customers[i+j];
            }
        }
        m = max(m,k+s);

       }
       return m;

    }
};