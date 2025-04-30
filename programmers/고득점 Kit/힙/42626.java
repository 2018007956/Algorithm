import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int cnt = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : scoville) {
            pq.offer(num);
        }

        while(pq.stream().anyMatch(x->x<K)) { // (pqScov.size() > 1 && pqScov.peek() < K)
            if(pq.size()==1) return -1;

            pq.offer(pq.poll() + pq.poll()*2);
            cnt++;
        }
        return cnt; // pq.peek() >= K ? cnt : -1;
    }
}