
bool cmp(pair<int,string>p1,pair<int,string>p2){
        return p1.first>=p2.first;
    }
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<int,string>> v;
        for(int i =0;i<names.size();i++){
            pair<int,string>p3 = make_pair(heights[i],names[i]);
            v.push_back(p3);
        }
        vector<string>nw;
        sort(v.begin(),v.end(),cmp);
        for(auto k:v){
            nw.push_back(k.second);
        }
        return nw;
    }
};