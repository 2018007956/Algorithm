import java.util.*;
class Solution {
    List<Integer>[] graph;
    int[] distance;
    int maxDist = 0;
    
    public void bfs() {
        Queue<Integer> q = new LinkedList<>();
        q.offer(1); 
        distance[1] = 0;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int next : graph[cur]) {
                if (distance[next] == -1) {
                    distance[next] = distance[cur] + 1;
                    q.offer(next);
                    maxDist = distance[next];
                }
            }
        }
    }
    
    public int solution(int n, int[][] edge) {
        graph = new ArrayList[n+1];
        for (int i=0; i<n+1; i++) graph[i] = new ArrayList<>();
        distance = new int[n+1];
        Arrays.fill(distance, -1);
        
        for (int[] e : edge) {            
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        
        bfs();
        
        // int maxDist = 0;
        // for (int d : distance) {
        //     maxDist = Math.max(maxDist, d);
        // }
        
        int cnt = 0;
        for (int d : distance) {
            if (d == maxDist) cnt++;
        }
        
        return cnt;
    }
}