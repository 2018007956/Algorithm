#include<bits/stdc++.h>
using namespace std;
int N;
string pattern, test;
vector<string> split(string input, string delimiter){
    vector<string> result;
    auto end = 0;
    while((end=input.find(delimiter)) != string::npos){
        result.push_back(input.substr(0, end));
        input.erase(0, end+delimiter.size());
    }
    result.push_back(input);
    return result;
}
int main(){
    cin >> N;
    cin >> pattern;
    vector<string> p = split(pattern, "*");
    for(int i=0;i<N;i++){
        cin >> test;
        // 반례 고려 : size 문제
        // 이 조건문 없으면 런타임 에러(out of range)발생
        if(p[0].size() + p[1].size() > test.size()){
            cout << "NE" << endl;
        }else{
            if(p[0]==test.substr(0, p[0].size()) and p[1]==test.substr(test.size()-p[1].size())){
                cout << "DA" << endl;
            }
            else cout << "NE" << endl;
        }
    }
}

// split 대신 find 사용
#include<bits/stdc++.h>
using namespace std;
int N;
string pattern, test, pre, suf;
int main(){
    cin >> N;
    cin >> pattern;
    int pos = pattern.find('*');
    pre = pattern.substr(0, pos);
    suf = pattern.substr(pos + 1);
    for(int i=0; i<N; i++){
        cin >> test;
        if(pre.size() + suf.size() <= test.size() and 
            pre==test.substr(0, pre.size()) and suf==test.substr(test.size()-suf.size())){
            cout << "DA" << endl;
        }
        else cout << "NE" << endl;
    }
}