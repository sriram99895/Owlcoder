class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int n = arr.size();
        int count = 0;
        int sum =0;
        for(int i = 0;i<k;i++){
            sum+=arr[i];
        }
        int avg = sum/k;
        if(avg>=threshold){
                count++;
            }

        cout<<sum << endl;;
        for(int i = k;i<n;i++){
            sum-=arr[i-k];
            sum+=arr[i];
            cout << sum << endl;
            int avg = sum/k;
            // cout << avg<<endl;
            if(avg>=threshold){
                count++;
            }
        }
        return count;
    }
};