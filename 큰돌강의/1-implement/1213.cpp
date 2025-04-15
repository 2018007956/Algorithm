#include<bits/stdc++.h>
using namespace std;
string s;
map<char, int> dict;
int main(){
    cin >> s;
    for(char a : s) dict[a]++;

    int oddCount = 0;
    char midChar = 0; // 중앙에 올 문자
    for (auto x : dict) {
        if (x.second % 2 != 0) {
            oddCount++;
            midChar = x.first;
        }
    }

    if (oddCount > 1) {
        cout << "I'm Sorry Hansoo" << endl;
        return 0;
    }

    string ret, ret2;
    for(auto x : dict){
        ret += string(x.second/2, x.first);
    }
    ret2 = ret;
    if (oddCount == 1) ret2 += midChar;
    reverse(ret.begin(), ret.end());
    ret2 += ret;
    cout << ret2 << endl;
    return 0; 
}
// string(count, character) : count번 반복한 character로 구성된 문자열이 만들어짐

// 큰돌 풀이
#include<bits/stdc++.h>
using namespace std;
string s, ret;
int cnt[200], flag;
char mid;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> s;
    for(char a : s) cnt[a]++;
    for(int i='Z'; i>='A'; i--){
        if(cnt[i]){
            if(cnt[i] & 1){ // %2==1처럼 &&1도 홀수체크
                mid = char(i);
                flag++;
                cnt[i]--; // 3개가 있을 때 2개로 만들고 하나 mid는 나중 붙임
            }
            if(flag==2) break;
            for(int j=0; j<cnt[i]; j+=2){
                ret = char(i)+ret;
                ret += char(i);
            }
        }
    }
    if(mid) ret.insert(ret.begin()+ret.size()/2, mid);
    if(flag==2) cout << "I'm Sorry Hansoo\n";
    else cout << ret << endl;
}