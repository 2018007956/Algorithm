class Solution {
    int maxCnt = 0;
    int[][] dungeons;
    boolean[] visited;
    
    public void dfs(int depth, int k) {
        maxCnt = Math.max(maxCnt, depth);
        
        for (int i=0; i<dungeons.length; i++) {
            if (!visited[i] && k>=dungeons[i][0]) {
                visited[i] = true;
                dfs(depth+1, k-dungeons[i][1]);
                visited[i] = false;
            }
        }
    }
    
    public int solution(int k, int[][] dungeons) {
        this.dungeons = dungeons;
        this.visited = new boolean[dungeons.length];
        
        dfs(0, k);
        
        return maxCnt;
    }
}
/*
처음에는 종료 조건을 아래와 같이 작성
if (k < 0 || depth==dungeons.length) {
    maxCnt = Math.max(maxCnt, depth);
    return;
} 
이렇게 하면, 끝났다고 판단되는 순간에만 갱신하는데
depth == dungeons.length가 아니어도 
모든 남은 던전이 조건을 만족하지 않아 더 이상 탐험 못하는 경우가 존재
 */