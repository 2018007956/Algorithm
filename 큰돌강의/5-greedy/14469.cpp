#include<bits/stdc++.h>
using namespace std;
int n, a, b, ret;
vector<pair<int, int>> v;
int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> a >> b;
        v.push_back({a, b});
    }
    sort(v.begin(), v.end());
    for(auto [a, b] : v){
        if(a >= ret) ret = a + b;
        else ret += b;
    }
    cout << ret << '\n';
    return 0;
}