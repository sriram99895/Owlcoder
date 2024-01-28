//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    public:
    vector<int> find(int arr[], int n , int x )
    {
        // code here
        int f = -1;
        int i =0;
        int j = n-1;
        while(i<=j){
           int mid = i+(j-i)/2;
           if(arr[mid] ==x){
               f = mid;
              j = mid - 1;
              
           }
           else if(arr[mid]<x){
               i = mid+1;
           }
           else{
               j = mid-1;
               
           }
           
        }
        int s = -1;
        int l =0;
        int h = n-1;
        while(l<=h){
           int m = l+(h-l)/2;
           if(arr[m] ==x ){
               s = m;
               l = m+1;
              
           }
           else if(arr[m]<x){
               l = m+1;
           }
           else{
               h = m-1;
               
           }
           
        }
        vector<int> v;
        v.push_back(f);
        v.push_back(s);
        return v;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,x;
        cin>>n>>x;
        int arr[n],i;
        for(i=0;i<n;i++)
        cin>>arr[i];
        vector<int> ans;
        Solution ob;
        ans=ob.find(arr,n,x);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
    return 0;
}



// } Driver Code Ends