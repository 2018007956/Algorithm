import java.util.*;
class Solution {
    List<String> answer = new ArrayList<>();
    boolean[] visited;
    String[][] tickets;

    public String[] solution(String[][] tickets) {
        this.tickets = tickets;
        this.visited = new boolean[tickets.length];

        Arrays.sort(tickets, (a, b) -> {
            if (!a[0].equals(b[0])) return a[0].compareTo(b[0]);
            return a[1].compareTo(b[1]);
        });

        dfs(new ArrayList<>(List.of("ICN")));
        return answer.toArray(new String[0]);
    }

    public void dfs(List<String> path) {
        if(path.size()==tickets.length+1) {
            if(answer.isEmpty()) {
                answer = new ArrayList<>(path);
            }
            return;
        }

        for(int i=0; i<tickets.length; i++) {
            if(!visited[i] && path.get(path.size()-1).equals(tickets[i][0])) {
                visited[i] = true;
                path.add(tickets[i][1]);
                dfs(path);
                path.remove(path.size()-1);
                visited[i] = false;
            }
        }
    }
}

// 다른 사람 풀이
import java.util.ArrayList;
import java.util.Collections;
class Solution {
    static ArrayList<String> answer = new ArrayList<>();
    static boolean[] visited;

    public String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];
        DFS(0, "ICN", "ICN", tickets);
        Collections.sort(answer);
        String[] temp = answer.get(0).split(" ");
        return temp;
    }

    private static void DFS(int cnt, String icn, String word, String[][] tickets) {
        if (cnt == tickets.length) {
            answer.add(word);
        } else {
            for (int i=0; i<tickets.length; i++) {
                if (!visited[i] && tickets[i][0].equals(icn)) {
                    visited[i] = true;
                    DFS(cnt+1, tickets[i][1], word+" "+tickets[i][1], tickets);
                    visited[i] = false;
                }
            }
        }
    }
}