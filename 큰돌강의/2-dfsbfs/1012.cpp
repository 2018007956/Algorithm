#include<bits/stdc++.h>
using namespace std;
int T, m, n, k, x, y, cnt;
int board[50][50], visited[50][50];
vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
void dfs(int y, int x){
    visited[y][x] = 1;
    for(auto [dy, dx] : dir){
        int ny = y + dy;
        int nx = x + dx;
        if(0<=ny and ny<n and 0<=nx and nx<m and board[ny][nx]==1 and not visited[ny][nx]){
            dfs(ny, nx);
        }
    }
}
int main(){
    cin >> T;
    while(T--){
        cin >> m >> n >> k;
        cnt = 0;
        memset(board, 0, sizeof(board));
        memset(visited, 0, sizeof(board));
        while(k--){
            cin >> x >> y;
            board[y][x] = 1;
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(board[i][j]==1 and not visited[i][j]){
                    dfs(i, j);
                    cnt++;
                }
            }
        }
        cout << cnt << endl;
    }
}