//clost strings or not q - 1657
#include<bits/stdc++.h>
using namespace std; 
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        map<char,int> fm;
        map<char,int> sm;

        for(auto it: word1){
            fm[it]++;
        }
        for(auto it:word2){
            sm[it]++;
        }
        vector<int> v1;
        vector<int> v2;
        for(auto it:fm){
            auto key = it.first;
            auto it2 = sm.find(key);
            if(it2!= sm.end()){
                v1.push_back(it.second);
                v2.push_back(it2->second);
            }
            else{
                return 0;
            }
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        for(int i = 0;i<v1.size();i++){
             if (v1[i] != v2[i]){
                 return 0;
             }
        }
        return 1;
    }
};