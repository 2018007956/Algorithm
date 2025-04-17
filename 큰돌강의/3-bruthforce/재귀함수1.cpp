/* 재귀함수를 활용한 완전탐색
[예제] 승철이의 문단속
승철이는 도쿄 위의 빨간 구름위에 올라가있다. 이 구름은 그대로 내버려두면 땅으로 떨어져 100만명의 사상자가 발생한다.
구름을 멈추는 방법은 구름의 특정 위치에 요석을 꽂으면 된다. 해당 위치에는 숫자가 표기되어있고 몇 개를 골라 숫자의 합이 "소수"가 될 때 구름은 멈춘다.
총 몇 개의 경우의 수가 있는지 말해라. N개의 요석 후보의 숫자와 다음 줄에 해당 숫자들이 나온다. N <= 100
Input 1> 
10
24 35 38 40 49 59 60 67 83 98
*/
#include<bits/stdc++.h>
using namespace std;
int n, temp;
vector<int> v;
bool check(int n){
    if(n <= 1) return 0;
    if(n == 2) return 1;
    if(n % 2 == 0) return 0;
    for(int i=2; i*i<=n; i++){
        if(n%i==0) return 0;
    }
    return 1;
}
int go(int idx, int sum){
    if(idx == n){
        // cout << "SUM" << sum << endl;
        return check(sum);
    }
    return go(idx+1, sum+v[idx]) + go(idx+1, sum);
}
int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> temp;
        v.push_back(temp);
    }
    cout << go(0, 0) << endl;
    return 0;
}