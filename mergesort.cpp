#include<bits/stdc++.h>
using namespace std;
void merge(int arr[],int left,int mid,int right){
    int leftsize = mid-left+1;
    int rightsize = right-mid;
    int leftarr[leftsize];
    int rightarr[rightsize];
    for(int i = 0;i<leftsize;i++){
        leftarr[i] = arr[left+i];
    }
    for(int j =0;j<rightsize;j++){
        rightarr[j] = arr[mid+1+j];
    }
    int leftpoint = 0;
    int rightpoint = 0;
    int arrpoint = left;
    while(leftpoint<leftsize && rightpoint<rightsize ){
        if(leftarr[leftpoint]<rightarr[rightpoint]){
            arr[arrpoint] = leftarr[leftpoint];
            leftpoint++;
        }
        else{
            arr[arrpoint] = rightarr[rightpoint];
            rightpoint++;
        }
        arrpoint++;
    }

    while(leftpoint<leftsize){
        arr[arrpoint] = leftarr[leftpoint];
        leftpoint++;
        arrpoint++;

    }
     while(rightpoint<rightsize){
        arr[arrpoint] = rightarr[rightpoint];
        rightpoint++;
        arrpoint++;
        
    }
}
void mergesort(int arr[],int begin, int end){
     if(begin>=end){
        return;
     }
     int mid = (begin+end)/2;
     mergesort(arr,begin,mid);
     mergesort(arr,mid+1,end);
     merge(arr,begin,mid,end );

}
int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i =0;i<n;i++){
        cin >> arr[i];
    }
    mergesort(arr,0,n-1);
    for(int i =0;i<n;i++){
        cout << arr[i]<<" ";
    }
}