class Solution{
public:
    int remove_duplicate(int ar[],int n){
        // code here
        int i =0;
        int j = i+1;
        while(j<n){
            if(ar[i] == ar[j]){
                j++;
                
            }
            else if(ar[i]!= ar[j]){
                swap(ar[i+1],ar[j]);
                i+=1;
                j+=1;
                
            }
        }
        return i+1;
    }
};