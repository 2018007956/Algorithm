#include<bits/stdc++.h>
using namespace std;
const int max_n = 104;
int n, m;
vector<pair<int, int>> dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int board[max_n][max_n], visited[max_n][max_n];
void bfs(int y, int x){
    queue<pair<int, int>> q;
    q.push({y, x});
    visited[y][x] = 1;
    while(!q.empty()){
        tie(y, x) = q.front(); q.pop();
        for(auto [dy, dx] : dir){
            int ny = y + dy;
            int nx = x + dx;
            if(0<=ny && ny<n and 0<=nx && nx<m and not visited[ny][nx] and board[ny][nx]==1){
                visited[ny][nx] = visited[y][x] + 1;
                q.push({ny, nx});
            }
        }
    }
}
int main(){
    cin >> n >> m;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%1d", &board[i][j]); // 1글자만 읽어서 정수로 변환
        }
    }
    bfs(0, 0);
    cout << visited[n-1][m-1] << endl;
}
/*
auto [a, b] = q.front(); : 새로운 변수 y, x 생성 (기존 변수와 이름 겹치면 안 됨)
tie(a, b) = q.front(); : 이미 있는 변수에 값을 대입할 때 사용

board 숫자가 공백으로 구분되어 있으면 %d로도 가능한데, 
한 줄에 숫자가 붙어서 들어오는 경우 %1d로 받아야 한 자리씩 읽어옴
*/