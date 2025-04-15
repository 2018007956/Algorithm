#include<bits/stdc++.h>
using namespace std;
int n, cnt;
string s;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for(int i=0;i <n; i++){
        cin >> s;
        stack<char> stk;
        for(char a : s){
            if(stk.size() && stk.top()==a) stk.pop();
            else stk.push(a);
        }
        if(stk.empty()) cnt++;
    }
    cout << cnt << endl;
}
/*
문제를 봤을 때 풀이법이 떠오르지 않는다면 <도식화>를 시켜라
90도 회전해보거나 뒤집거나 하나를 더 붙여보면서 아이디어 잡아나가기
* 문제에 '짝짓기', '폭발'이라는 단어가 있으면 => stack을 생각해보기


vector는 [] 연산자에 음수 인덱스를 지원하지 않음
v[-1] 대신 v.back() 사용

vector 대신 stack 사용 가능
*/