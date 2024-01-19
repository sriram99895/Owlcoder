//chocolate fiest in hacker rank
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);
const int mod = 1e9+7;
// const int N = 1e5+1;
// vector<int> fact(N);
// vector<int> infact(N);
int pow(int a, int b){
    int p = 1;
    while(b){
        if(b%2 ==1){
            p*=a;
            p%= mod;
            
        }
        a = (a*a)%mod;
        b= b>>1;
    }
    return p;
}
// void prefact(){
//     fact[0] =1;
//     infact[0] = 1;
//     for(int i =1;i<N;i++){
//         fact[i] = fact[i-1]*i;
//         infact[i] = pow(fact[i],mod-2);
//     }
    
// }

/*
 * Complete the 'solve' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

int solve(vector<int> a) {
    int ec=0;
    int oc = 0;
    for(int i = 0;i<a.size();i++){
        if(a[i]%2 ==0){
            ec++;
        }
        else{
            oc++;
        }
    }
    long long ecom = 0;
    long long ocom  = 0;
    if(ec!=0 && oc!=0){ 
        ocom = (((pow(2,oc-1))%mod))-1;
        ecom = ((pow(2,ec))%mod)-1;
        long long total =((ecom + ocom)%mod + (ecom * ocom)%mod)%mod;
    // cout<< total;
        return  total;
    };
    
    ecom = ((pow(2,ec))%mod)-1;
    return  ecom%mod;

}
