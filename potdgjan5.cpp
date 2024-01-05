#include<bits/stdc++.h>
using namespace std;
class mysol{
    public:
    

int totalways(int n){
if(n == 1) return 4;
	    if(n == 2) return 9;
	    long arr[n];
	    arr[0] = 2;
	    arr[1] = 3;
	    long mod  = long(1e9 + 7);
	    for(int i = 2;i<n;i++){
	        arr[i] = (arr[i-1]+arr[i-2])%mod;
	    }
	    return nt((arr[n-1]*arr[n-1])%mod);
    }
    };

int main(){
	int n ;
	cin >> n;
	mysol ob;
	int k = ob.totalways(n);
	cout << k;



}