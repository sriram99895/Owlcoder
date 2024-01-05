#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int arr[n];
    int dp[n];
    int ov = 0;
    for(int i = 0;i<n;i++){
        cin >> arr[i];
        dp[i] = 1;
    }
    for(int i =0;i<n;i++){
        int max = 0;
        for(int j = 0;j<i;j++){
         if (arr[j]<arr[i]){
            if(max<dp[j]) {
                max = dp[j];
            }
         }
        }
        dp[i]+=max;
        if (dp[i]>ov){
            ov = dp[i];
        }
    }
    for(int i = 0;i<n;i++){
        cout << dp[i]<< " ";
    }
    cout << ov;

   

}