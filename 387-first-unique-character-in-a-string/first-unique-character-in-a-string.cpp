class Solution {
public:
    int firstUniqChar(string s) {
    reverse(s.begin(),s.end());
    unordered_map<char,int> m;
    for (int i = 0;i<s.size();i++){
        m[s[i]]++;
    }
    // reverse(m.begin(),m.end());
    char val = '-';
    for(auto it:m){
        if (it.second == 1){
            val = it.first;
            break;
        }
    }
    reverse(s.begin(),s.end());

    for (int i =0;i<s.size();i++){
        if(s[i]==val){
            return i;
        }
    }
    return -1;



    }
};