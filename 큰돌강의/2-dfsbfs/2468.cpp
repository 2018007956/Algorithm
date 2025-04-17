#include<bits/stdc++.h>
using namespace std;
int n, cnt, ret;
int board[100][100], visited[100][100];
vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
void dfs(int y, int x, int d){
    visited[y][x] = 1;
    for(auto [dy, dx] : dir){
        int ny = y + dy;
        int nx = x + dx;
        if(0<=ny && ny<n && 0<=nx && nx<n and board[ny][nx] > d and not visited[ny][nx]){
            dfs(ny, nx, d);
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> board[i][j];
        }
    }
    for(int d=0; d<101; d++){
        memset(visited, 0, sizeof(visited));
        cnt = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] > d and not visited[i][j]){
                    dfs(i, j, d);
                    cnt++;
                }
            }
        }
        ret = max(ret, cnt);
    }
    printf("%d\n", ret);
}
/*
1. ios_base::sync_with_stdio(false);
2. cin.tie(NULL); cout.tie(NULL);
코드는 scanf 사용 시 문제 발생
1번 코드는 C++의 iostream과 C의 stdio 라이브러리 간의 동기화를 끊는 명령이다. 
이렇게 하면 cin/cout의 성능이 향상되지만, scanf/printf와 cin/cout을 혼용해서 사용할 수 없게 된다.
*/