bool cmp(pair<char,int>&p,pair<char,int>&q){
    return p.second>q.second;
    
}
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char,int> m;
    for(int i = 0;i<s.size();i++){
        m[s[i]]++;
    }
    vector<pair<char,int>> v;
    for(auto it:m){
        v.push_back(it);
    }
    sort(v.begin(),v.end(),cmp);
    // sort(m.begin(),m.end(),cmp);
    // for(auto it:v){
    //     cout << it.first<<" "<<it.second<<endl;
    // }
    string re = "";
    for(auto it:v){
        for (int i =0;i<it.second;i++){
            re+=it.first;
        }
        
    }
    // reverse(re.begin(),re.end());
    return re;   
    }
};
 