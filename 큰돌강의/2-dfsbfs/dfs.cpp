void dfs(int here){
    visited[here] = 1;
    for(int there : adj[here]){
        if(visited[there]) continue;
        dfs(there);
    }
}


void dfs(int here){
    if(visited[here]) return;
    visited[here] = 1;
    for(int there : adj[here]){
        dfs(there);
    }
}