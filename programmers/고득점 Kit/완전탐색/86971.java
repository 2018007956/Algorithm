import java.util.*;
class Solution {
    List<List<Integer>> graph;
    boolean[] visited;
    
    public int bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        visited[start] = true;
        q.add(start);
        int cnt = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            cnt++;

            for (int adj : graph.get(cur)) {
                if (!visited[adj]) {
                    visited[adj] = true;
                    q.add(adj);
                }
            }    
        }
        
        return cnt;
    }
    
    public int solution(int n, int[][] wires) {
        int minVal = 100;
        
        for (int j=0; j<wires.length; j++) { 
            graph = new ArrayList<>();
            for (int i=0; i<=n; i++) graph.add(new ArrayList<>());
            
            int cut1 = wires[j][0];
            int cut2 = wires[j][1];
            for (int i=0; i<wires.length; i++) {
                if (!(wires[i][0] == cut1 && wires[i][1] == cut2) && !(wires[i][0] == cut2 && wires[i][1] == cut1)) { // 연결 끊기
                    graph.get(wires[i][0]).add(wires[i][1]);
                    graph.get(wires[i][1]).add(wires[i][0]);
                }
            }
            
            visited = new boolean[n+1];
            int res = bfs(cut1);
            minVal = Math.min(minVal, Math.abs(res - (n-res)));
        }
        
        return minVal;
    }
}

// 다른 사람 풀이) 자식 수만 가지고 구하는 방법
// DFS 재귀 호출마다 서브트리를 계산하면서 그 간선을 끊었을 경우를 고려
import java.util.*;
class Solution {
    int N, min;
    int[][] map;
    boolean[] visited;
    int dfs(int n) {
        visited[n] = true;
        int child = 1;
        for (int i=1; i<=N; i++) {
            if (!visited[i] && map[n][i] == 1) {
                child += dfs(i);
            }
        }
        min = Math.min(min, Math.abs(child - (N - child)));
        return child;
    }
    public int solution(int n, int[][] wires) {
        N = n;
        min = n;
        map = new int[n+1][n+1];
        visited = new boolean[n+1];
        for (int[] wire : wires) {
            int a = wire[0], b = wire[1];
            map[a][b] = map[b][a] = 1;
        }
        dfs(1);
        return min;
    }
}
/* 이 코드를 통해 배운점
- 양방향 그래프 구성할 때 : map[a][b] = map[b][a] = 1;
- dfs(1)로만 호출해도, 서브 트리를 탐색하면서 모든 경우를 고려할 수 있음
 */