#include<bits/stdc++.h>
using namespace std;
int t, n;
string a, b;
int main(){
    cin >> t;
    while(t--){
        cin >> n;
        map<string, int> clothes;
        for(int i=0; i<n; i++){
            cin >> a >> b;
            clothes[b]++;
        }
        long long ret=1;
        for(auto c : clothes){
            ret *= c.second + 1;
        }
        cout << ret-1 << endl;
    }
}
// 경우의 수는 수가 커질 수 있으므로 long long 으로 선언