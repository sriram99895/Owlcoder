class Solution {
public:
    int countPrimes(int n) {
        
        if(n == 0 || n == 1){
            return 0;
        }
       int v[n];
       for(int i = 0;i<n;i++){
           v[i] = 1;
       }
       int k = sqrt(n);
       v[0] = 0;
       v[1] = 0;
    // for(int i =0;i<v.size();i++){
    //       cout << v[i];
    //    }   
    //    cout << endl;
       for(int i =2;i<=k;i++){
           if(v[i] == 1){
               for(int j = i*i;j<n;j+=i){
                   v[j] = 0;
               }
           }
       }
       int c = 0;
       for(int i =2;i<n;i++){
           if(v[i] == 1){
               c+=1;
           }
       }
    //    cout << endl;
       return c;
    }
};