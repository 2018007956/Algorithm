import java.util.*;
class Solution {
    public void dfs(int cur, int n, int[][] computers, boolean[] visited) {
        visited[cur] = true;
        for(int i=0; i<n; i++) {
            if(cur!=i && computers[cur][i]==1 && !visited[i]) {
                dfs(i, n, computers, visited);
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for(int i=0; i<n; i++) {
            if(!visited[i]) {
                dfs(i, n, computers, visited);
                answer++;
            }
        }
        return answer;
    }
}