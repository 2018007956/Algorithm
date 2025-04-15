#include<bits/stdc++.h>
using namespace std;
int n, m, a[15001], cnt;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    for(int i=0;i<n;i++) cin >> a[i];
    // 이 if문은 없어도 됨. just 예외처리
    if(m > 200000) cout << 0 << endl;
    else{
        // Combination
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if(a[i] + a[j] == m) cnt++;
            }
        }
        cout << cnt << endl;
    }
}

// 재귀를 통한 풀이
#include<bits/stdc++.h>
using namespace std;
int n, m, a[15001], cnt;
void combi(int idx, vector<int> & v){
    if(v.size()==2){
        if(a[v[0]]+a[v[1]]==m) cnt++;
        return;
    }
    for(int i=idx+1; i<n; i++){
        v.push_back(i);
        combi(i, v);
        v.pop_back();
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    for(int i=0;i<n;i++) cin >> a[i];
    vector<int> v;
    combi(-1, v);
    cout << cnt << endl;
}