// 1. erase를 이용한 풀이
#include<bits/stdc++.h>
using namespace std;
string s, bomb, ret;
int main(){
    cin >> s >> bomb;
    for(char a : s){
        ret += a;
        if(ret.size() >= bomb.size() && ret.substr(ret.size()-bomb.size(), bomb.size()) == bomb){
            ret.erase(ret.end() - bomb.size(), ret.end());
        }
    }
    if(!ret.size()) cout << "FRULA" << "\n";
    else cout << ret << "\n";
    return 0;
}


// 2. stack을 활용한 풀이
// 문제에서 "폭발, 짝짓기" 단어나오면 stack 사용 가능성 높음
#include<bits/stdc++.h>
using namespace std;
string s, bomb, ret;
stack<char> stk;
int main(){
    cin >> s >> bomb;
    for(char a : s){
        stk.push(a);
        if(stk.size() >= bomb.size() && stk.top() == bomb[bomb.size()-1]){
            string ss = "";
            for(char i : bomb){
                ss += stk.top(); stk.pop();
            }
            reverse(ss.begin(), ss.end());
            if(bomb != ss){
                for(int i : ss){
                    stk.push(i);
                }
            }
        }
    }
    if(stk.size()==0){
        cout << "FRULA\n";
    }else{
        while(stk.size()){
            ret += stk.top(); stk.pop();
        }
        reverse(ret.begin(), ret.end());
        cout << ret << "\n";
    }
    return 0;
}