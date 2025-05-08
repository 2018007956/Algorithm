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