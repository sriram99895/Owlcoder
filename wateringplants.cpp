//2079
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
         int nc = capacity;
         int s = 0;
        for(int i =0;i<plants.size();i++){
            if(plants[i]<= capacity){
                s+=1;
              capacity = capacity-plants[i];  
              cout << s<< endl;
            }
            else{
                s+=(i+i+1);
                cout << s<<endl;
                capacity = nc-plants[i];
            }
        }
        return s;
    }
};