class Solution {
public:
    string removeStars(string st) {
        stack<char> s;
        for(auto it:st){
            if(it == '*'){
                s.pop();
            }
            else{
                s.push(it);
            }
        }
        string ne = "";
        while(!s.empty()){
            auto t=s.top();
            ne+=t;
            s.pop();
        }
        reverse(ne.begin(),ne.end());
        return ne;
        
    }
};