#include<bits/stdc++.h>
using namespace std;
string s, ret;
int main(){
    getline(cin, s);
    for(int i=0; i<s.size(); i++){
        if('A' <= s[i] && s[i] <= 'Z'){
            ret += char('A' + (s[i]-'A'+13) % 26);
        } else if('a' <= s[i] && s[i] <= 'z'){
            ret += char('a' + (s[i]-'a'+13) % 26);
        } else {
            ret += s[i];
        }
    }
    cout << ret << endl;
}