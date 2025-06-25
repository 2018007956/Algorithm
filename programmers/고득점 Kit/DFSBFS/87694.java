import java.util.*;
class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = Integer.MAX_VALUE;
        Boolean[][] map = new Boolean[102][102];
        int[] dx = new int[] {1, 0, -1, 0};
        int[] dy = new int[] {0, 1, 0, -1};
        characterX *= 2;
        characterY *= 2;
        itemX *= 2;
        itemY *= 2;
        for(int i=0; i<rectangle.length; i++) {
            for(int j=0; j<rectangle[i].length; j++) rectangle[i][j] *= 2;
            // 직사각형 내부는 0, 테두리는 1로 유지
            for(int x=rectangle[i][0]; x<=rectangle[i][2]; x++) {
                for(int y=rectangle[i][1]; y<=rectangle[i][3]; y++) {
                    // 아직 내부로 확정되지 않았을 경우 갱신
                    if(map[x][y] != Boolean.FALSE) {
                        // 가장자리 좌표와 하나라도 겹치면 -> 사각형 테두리 선분 위
                        map[x][y] = (x==rectangle[i][0] || x==rectangle[i][2] ||
                                y==rectangle[i][1] || y==rectangle[i][3]);
                    }
                }
            }
        }

        // BFS
        Queue<int[]> queue = new LinkedList<>();
        map[characterX][characterY] = Boolean.FALSE;
        queue.offer(new int[] {characterX, characterY, 0});
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            if(cur[0] == itemX && cur[1] == itemY) {
                answer = Math.min(answer, cur[2]/2);
            }

            for(int i=0; i<4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if(nx>=2 && nx<=100 && ny>=2 && ny<=100 && map[nx][ny]==Boolean.TRUE) {
                    map[nx][ny] = Boolean.FALSE;
                    queue.offer(new int[] {nx, ny, cur[2]+1});
                }
            }
        }
        return answer;
    }
}
/*
Boolean.FALSE, Boolean.TRUE를 false, true로 쓰게 되면 다음과 같은 에러 발생
Exception in thread "main" java.lang.NullPointerException
	at Solution.solution(Unknown Source)
	at SolutionTest.lambda$main$0(Unknown Source)
	at SolutionTest$SolutionRunner.run(Unknown Source)
	at SolutionTest.main(Unknown Source)

원인 : 자바에서는 객체 배열을 생성하면 기본값이 null로 초기화됨.
그래서 map[x][y]에 접근해서 값을 쓰기 전에 map[x][y] = true; 와 같은 명시적 할당이 없으면, map[x][y]는 null 상태이다.
그래서 if(map[x][y] != false) 이 코드의 경우, map[x][y]가 null이면 null.booleanValue()가 호출되어 NullPointerException이 발생

해결 : Boolean.FALSE / Boolean.TRUE 사용
    map[x][y] = Boolean.TRUE;로 직접 할당하면 null이 아니므로 문제가 없음

cf) boolean[][]로 선언 (기본형 배열):
    기본형 배열은 자동으로 false로 초기화되므로 null 문제 없음
    가장 권장되는 방식
    근데 이 문제에서는 이렇게 선언하면 결과값이 MAX_VALUE 그대로 나옴

    >> Boolean은 null 체크가 가능 → 로직에 유연성 있음
    >> boolean은 초기값이 false → != false는 항상 false
       수정하려면 상태 추적용 visited 배열 등 추가 로직 필요
 */

// 다른 풀이
import java.util.LinkedList;
import java.util.Queue;
class Solution {
    static int[][] map;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int answer;
    static int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        map = new int[101][101];
        for (int[] r : rectangle) {
            fill(2*r[0], 2*r[1], 2*r[2], 2*r[3]);
            bfs(2*characterX, 2*characterY, 2*itemX, 2*itemY); // 2배배
            return answer;
        }
    }

    // 내부와 테두리를 구분
    public void fill(int x1, int y1, int x2, int y2) {
        for (int i=x1; ix<x2; i++) {
            for (int j=y1; j<=y2; j++) {
                if (map[i][j] == 2) continue;
                map[i][j] = 2;
                if (i==x1||i==x2||j==y1||j==y2) map[i][j] = 1;
            }
        }
    }

    public void bfs(int startX, int startY, int itemX, int itemY) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{startX, startY});
        int[][] cost = new int[101][101];
        cost[startX][startY] = 1;

        while (!q.isEmpty) {
            int[] move = q.poll();

            for (int i=0; i<4; i++) {
                int moveX = move[0] + dx[i];
                int moveY = move[1] + dy[i];

                if (0>moveX || 0>moveY || moveX>100 || moveY>100) continue;
                if (map[moveX][moveY] == 1 && cost[moveX][moveY] == 0) {
                    cost[moveX][moveY] = cost[move[0]][move[1]] + 1;
                    q.offer(new int[](moveX, moveY));
                }
            }
        }
        answer = cost[itemX][itemY]/2;
    }
}