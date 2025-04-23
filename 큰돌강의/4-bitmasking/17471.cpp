#include<bits/stdc++.h>
using namespace std;
const int INF = 987654321;
int n, people[11], m, temp, ret=INF, comp[11], visited[11];
vector<int> adj[11];
pair<int, int> dfs(int here, int value){
    visited[here] = 1;
    pair<int, int> ret = {1, people[here]}; // 연결된 컴포넌트 수, 인구수 총합
    for(int there : adj[here]){
        if(comp[there]==value and not visited[there]){
            pair<int, int> _temp = dfs(there, value);
            ret.first += _temp.first;
            ret.second += _temp.second;
        }
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i=1; i<=n; i++) cin >> people[i];

    // 양방향 간선 만들기
    for(int i=1; i<=n; i++){
        cin >> m;
        for(int j=0; j<m; j++){
            cin >> temp;
            adj[i].push_back(temp);
            adj[temp].push_back(i);
        }
    }

    // 모든 경우의 수 체크
    for(int i=1; i<(1<<n)-1; i++){
        fill(comp, comp+11, 0);
        fill(visited, visited+11, 0);
        int idx1=-1, idx2=-1; // 각 선거구의 탐색스타트지점
        // 시작 지점 색칠
        for(int j=0; j<n; j++){
            if(i&(1<<j)){
                comp[j+1] = 1;
                idx1 = j+1;
            } 
            else idx2 = j+1;
        }
        pair<int, int> comp1 = dfs(idx1, 1);
        pair<int, int> comp2 = dfs(idx2, 0);
        if(comp1.first+comp2.first==n) ret=min(ret, abs(comp1.second-comp2.second));
    }
    cout << (ret==INF ? -1 : ret) << '\n';
}