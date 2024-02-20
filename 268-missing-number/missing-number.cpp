class Solution {
public:
    int missingNumber(vector<int>& v) {
        int s = 0;
        for(int i=1;i<=v.size();i++){
            s^= i;
        }
        for(int i =0;i<v.size();i++){
            if (v[i]>0){
                s^=v[i];
            }

        }
        return s;
    }
};