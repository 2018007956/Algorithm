#include<bits/stdc++.h>
using namespace std;
vector<int> adj[100];
int visited[100];
void bfs(int here){
    queue<int> q;
    visited[here] = 1;
    q.push(here);
    while(q.size()){
        int here = q.front(); q.pop();
        for(int there : adj[here]){
            if(visited[there]) continue;
            visited[there] = visited[here] + 1;
            q.push(there);
        }
    }
}