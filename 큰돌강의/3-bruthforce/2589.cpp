#include<bits/stdc++.h>
using namespace std;
int m, n, mx, visited[54][54];
char board[54][54];
vector<pair<int, int>> dir = {{-1,0}, {1,0}, {0,1}, {0,-1}};
void bfs(int y, int x){
    memset(visited, 0, sizeof(visited));
    queue<pair<int, int>> q;
    visited[y][x] = 1;
    q.push({y, x});
    while(!q.empty()){
        tie(y, x) = q.front(); q.pop();
        for(auto [dx, dy] : dir){
            int nx = x + dx;
            int ny = y + dy;
            if(0<=ny&&ny<m&&0<=nx&&nx<n && board[ny][nx]=='L' && not visited[ny][nx]){
                visited[ny][nx] = visited[y][x] + 1;
                q.push({ny, nx});
                mx = max(mx, visited[ny][nx]-1);
            }
        }
    }
    return;
}
int main(){
    cin >> m >> n;
    for(int i=0;i<m; i++){
        for(int j=0; j<n; j++){
            cin >> board[i][j];
        }
    }
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(board[i][j]=='L'){
                bfs(i, j);
            }
        }
    }
    cout << mx << endl;
}