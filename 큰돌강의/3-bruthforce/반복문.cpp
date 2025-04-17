/* 반복문을 활용한 완전탐색 - for or while
[예제] 2400!! 2400!! 2400!!
트위치BJ 랄로는 2400이란 숫자를 좋아한다. 파카는 랄로의 수를 만들고자 하는데, 랄로의 수란 2400이 들어간 수를 말한다.
첫번째 랄로의 수는 2400이고 두번째 랄로의 수는 12400, 세번째 랄로의 수는 22400이다. 
N이 입력으로 주어졌을 때 N번째 랄로의 수를 구하라. N은 300이하로 주어진다.
*/
#include<bits/stdc++.h>
using namespace std;
int n, cnt;
// const int INF = 1e6;
int main(){
    cin >> n;
    int i = 2400;
    while(true){// for(int i=2400; i<INF; i++){
        string x = to_string(i);
        if(x.find("2400")!=string::npos){
            cnt++;
            if(n == cnt){
                cout << x << endl;
                break;
            }
            cout << cnt << " : " << x << endl;
        }
        i++;
    }
    return 0;
}