class Solution {
public:
    string fractionAddition(string expression) {
        istringstream in(expression);
        int num,deno;
        int nw = 0,dw = 1;
        char op;
        while(in>>num>>op>>deno){
           nw = nw*deno+num*dw;
           dw = dw*deno;
           int gcd = abs(__gcd(nw,dw));
           nw = nw/gcd;
           dw = dw/gcd;
        }
        cout<< nw<<dw;
        return to_string(nw)+"/"+to_string(dw);
        
    }
};