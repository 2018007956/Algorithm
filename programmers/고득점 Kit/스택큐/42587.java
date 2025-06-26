import java.util.*;
class Solution {
    class Pair {
        int idx;
        int val;
        
        Pair(int idx, int val) {
            this.idx = idx;
            this.val = val;
        }
    }    
    
    public int solution(int[] priorities, int location) {
        Queue<Pair> q = new LinkedList<>(Arrays.asList());
        for (int i=0; i<priorities.length; i++) {
            q.offer(new Pair(i, priorities[i]));
        }
        
        List<Integer> answerList = new ArrayList<>();
        int maxVal = Arrays.stream(priorities).max().getAsInt();
        while (!q.isEmpty()) {
            Pair x = q.poll();
            if (x.val != maxVal) {
                q.offer(x);
            } else {
                answerList.add(x.idx);
                maxVal = 0;
                for (Pair pair : q) {
                    if (pair.val > maxVal) maxVal = pair.val;
                }
            }
        }
        return answerList.indexOf(location)+1;
    }
}

// 다른 사람 풀이
import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int l = location;
    
        Queue<Integer> que = new LinkedList<Integer>();
        for(int p : priorities){
            que.add(p);
        }
        Arrays.sort(priorities);
        int size = priorities.length-1;
    
        while(!que.isEmpty()) {
            int x = que.poll();
            if (x == priorities[size - answer]) {
                answer++;
                l--;
                if (l<0) break;
            } else {
                que.add(x);
                l--;
                if (l<0) l = que.size()-1;
            }
        }
        return answer;
    }
}

// PriorityQueue 사용
import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int p : priorities){
            pq.add(p);
        }

        int answer = 1;
        while(!pq.isEmpty()) {
            for (int i=0; i<priorities.length; i++) {
                if (priorities[i] == pq.peek()) {
                    if (i == location) {
                        return answer;
                    }
                    pq.poll();
                    answer++;
                }
            }
        }

        return answer;
    }
}