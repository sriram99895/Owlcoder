//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:

    bool kPangram(string str, int k) {
        // code here
        // if(str.size()<26){
        //     return false;
        // }
        map<char,int>m;
        int c = 0;
        for(auto it:str){
            if (int(it)>=97 && int(it)<=127){
                m[it]++;
                c+=1;
            }
        }
        if(c<26){
            return false;
        }
        // cout << m.size();
        if(m.size() == 26){
            return true;
        }
        if(m.size()+k >=26) return true;
        return false;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        cin.ignore();
        string str;
        getline(cin, str);

        int k;
        cin >> k;

        Solution ob;
        bool a = ob.kPangram(str, k);
        if (a)
            cout << "true" << endl;
        else
            cout << "false" << endl;
    }
    return 0;
}
// } Driver Code Ends