/* 재귀함수를 활용한 완전탐색
[예제]
N과 N개의 자연수가 주어진다. 여기서 몇개의 숫자를 골라 합을 mod11을 했을 때 나오는 가장 큰 수를 구하라
Input1>
10
24 35 38 40 49 59 60 67 83 98
*/
#include<bits/stdc++.h>
using namespace std;
int n, temp, ret;
vector<int> v;
const int mod = 11;
int cnt = 0;
void go(int idx, int sum){
    if(ret == 10) return; // 백트래킹 : 11mod는 10이 최대 숫자이므로 해당 경우의 수 제거
    if(idx == n){
        ret = max(ret, sum % mod);
        cnt++;
        return;
    }
    go(idx+1, sum+v[idx]);
    go(idx+1, sum);
}
int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> temp;
        v.push_back(temp);
    }
    go(0, 0);
    cout << ret << endl;
    cout << cnt << endl;
    return 0;
}