//jan 4 potd in geek for geeks
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>> a[i];   
    }
    int emp[32];
    for(int i=0;i<=31;i++){
        int s = 0;
        for(int j =0;j<n;j++){
         int mask = 1<<i;
         if (a[j]&mask){
            s+=1;
         }
        }
        emp[i] = s;
    }
 for(int i = 0;i<=31;i++){
    cout << emp[i] << " ";
 }
 cout << endl;
int num = 0;
 for(int i =0;i<=31;i++){
    if(emp[i]%3!=0){
        int k = 1<<i;
        num = num|k;
    }
 }
 cout << num;
}