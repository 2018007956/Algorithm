#include<bits/stdc++.h>
using namespace std;
const int INF = 987654321;
int n, mp, mf, ms, mv;
int p, f, s, v, c, ret=INF;
struct Nutrient{
    int mp, mf, ms, mv, cost;
}nutrient[16];
map<int, vector<vector<int>>> ret_v;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    cin >> mp >> mf >> ms >> mv;
    for(int i=0; i<n; i++){
        cin >> nutrient[i].mp >> nutrient[i].mf >> nutrient[i].ms >> nutrient[i].mv >> nutrient[i].cost;
    }
    // N개의 음식에 대한 모든 경우의 수 = 2^N
    for(int i=0; i<(1<<n); i++){
        vector<int> select;
        p = f = s = v = c = 0;
        for(int j=0; j<n; j++){
            if(i&(1<<j)){
                select.push_back(j+1);
                p += nutrient[j].mp;
                f += nutrient[j].mf;
                s += nutrient[j].ms;
                v += nutrient[j].mv;
                c += nutrient[j].cost;
            }
        }
        if(p>=mp && f>=mf && s>=ms && v>=mv){
            if(c <= ret){
                ret = c;
                ret_v[ret].push_back(select);
            }
        }
    }

    if(ret==INF) cout << -1 << '\n';
    else{
        sort(ret_v[ret].begin(), ret_v[ret].end());
        cout << ret << '\n';
        for(int a : ret_v[ret][0]) cout << a << " ";
    }
}
/*
- 번호까지 저장하려면 ret = min(ret, c) 이 아니라 조건문으로 만들어야 함
- 같은 비용집합이 있을 수 있는데, 사전 순으로 빠른 것 출력하려면 그냥 asnwer = select 담는 방식으로는 안됨
    map<int, vector<vector<int>>> ret_v : 최소비용이라는 키에 집합 할당 & 집합이 여러개 일 수 있음
*/