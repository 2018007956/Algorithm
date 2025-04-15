#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll a, b, c;
ll go(ll a, ll b){
    if(b==1) return a % c;

    ll ret = go(a, b/2);
    ret = (ret * ret) % c;
    if(b%2) ret = ret * a % c;
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> a >> b >> c;
    cout << go(a, b) << endl;
}
/*
go(a, b/2) * go(a, b/2) % c 이렇게 하면 재귀 호출이 중복되면서 시간복잡도 증가하므로
변수 선언해서 한 번만 호출하도록 구현하기
*/