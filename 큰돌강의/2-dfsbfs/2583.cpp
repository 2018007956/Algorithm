#include<bits/stdc++.h>
using namespace std;
#define y1 aaaa  // y1 변수명 쓰려면 define 걸어줘야 함
int m, n, k, x1, y1, x2, y2;
int board[104][104], visited[104][104];
vector<pair<int, int>> dir = {{-1,0}, {1,0}, {0,1}, {0,-1}};
int bfs(int y, int x){
    queue<pair<int, int>> q;
    visited[y][x] = 1;
    q.push({y, x});
    int cnt = 1;
    while(!q.empty()){
        tie(y, x) = q.front(); q.pop();
        for(auto [dx, dy] : dir){
            int nx = x + dx;
            int ny = y + dy;
            if(0<=ny && ny<m && 0<=nx && nx<n && board[ny][nx]==0 && not visited[ny][nx]){
                visited[ny][nx] = 1;
                q.push({ny, nx});
                cnt++;
            }
        }
    }
    return cnt;
}
int main(){
    cin >> m >> n >> k;
    for(int i=0; i<k; i++){
        cin >> x1 >> y1 >> x2 >> y2;
        for(int x=x1; x<x2; x++){
            for(int y=y1; y<y2; y++){
                board[y][x] = 1;
            }
        }
    }
    vector<int> area;
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(board[i][j]==0 && not visited[i][j]){
                area.push_back(bfs(i, j));
            }
        }
    }
    cout << area.size() << endl;
    sort(area.begin(), area.end());
    for(auto x : area) cout << x << " ";
}

///////////////////////////////////////////////
// DFS로 구한다면
int dfs(int y, int x){
    visited[y][x] = 1;
    int cnt = 1;
    for(auto [dy, dx] : dir){
        int nx = x + dx;
        int ny = y + dy;
        if(0<=ny && ny<m && 0<=nx && nx<n && board[ny][nx]==0 && not visited[ny][nx]){
            cnt += dfs(ny, nx);
        }
    }
    return cnt;
}