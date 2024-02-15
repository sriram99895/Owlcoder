class Solution {
public:
    string removeDuplicates(string st) {
        stack<char> s;
        for(auto it:st){
            if(s.empty()){
                s.push(it);
            }
            else{
                auto k = s.top();
                if(k == it){
                    s.pop();

                }
                else{
                    s.push(it);
                }
            }
        }
        string ne = "";
        while(!s.empty()){
            auto it = s.top();
            ne+=it;
            s.pop();
        }
        reverse(ne.begin(),ne.end());
        return ne;
        
    }
};