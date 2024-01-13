#include<bits/stdc++.h>
using namespace std;
vector<int> seive(int n){
    long long k = sqrt(n);
    vector<int> v(k+1,1);
    for(int i = 2;i*i<=k;i++){
        if(v[i] == 1){
            for(int j = i*i;j<=k;j+=i){
                  v[j] = 0;

            }
        }
    }
    vector<int>nw;
    for(int i =2;i<v.size();i++){
        if(v[i] == 1){
            nw.push_back(i);
        }
    }
    return nw;


}
int main (){
    int l,r;
    cin >> l >> r;
    vector<int> v;
    v = seive(r);
    // for(auto it:v){
    //     cout<< it;
    // }
    vector<int> k(r-l+1,1);
    for(auto p:v){
        long long rm = (l/p)*p;
        if(rm<l){
            rm+=p;
        }
        for(long long m = rm;m<=r;m+=p){
            k[m-l] = 0;
        }

    }
    int p;
    for(long long i = l;i<=r;i++){
        if (k[i-l] == 1){
            p = p*i;
        }
    }
    cout << p;




}