//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int smallestSubWithSum(int x, vector<int>& arr) {
        
        // Your code goes here
        int n = arr.size();
        int sum = 0;
        int start = 0;
        int mini = 99999;
        int end;
        for(end = 0;end<n;end++){
            sum +=arr[end];
            while(sum>x ){
                mini = min(mini,end-start+1);
                sum-=arr[start];
                start++;
            }
        }
        if(mini == 99999){
            return 0;
        }
        return mini;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // Ignore the newline character after t

    while (t--) {
        vector<int> arr;
        int x;

        cin >> x;
        cin.ignore(); // Ignore the newline character after x

        string input;
        getline(cin, input); // Read the entire line for the array elements

        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution obj;
        cout << obj.smallestSubWithSum(x, arr) << "\n~\n";
    }

    return 0;
}
// } Driver Code Ends