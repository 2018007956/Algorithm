import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        List<Integer> deploy = new ArrayList<>();
        for(int i=0; i<progresses.length; i++){
            int days = (int) Math.ceil((100.0-progresses[i])/speeds[i]);
            deploy.add(days);
        }
        
        int cnt = 1;
        int cul_val = deploy.get(0);
        for(int i=1; i<progresses.length; i++){
            int val = deploy.get(i);
            if(val <= cul_val){
                cnt += 1;
            }else{
                answer.add(cnt);
                cnt = 1;
                cul_val = deploy.get(i);
            }
        }
        answer.add(cnt);
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}   
/* deploy 리스트를 안 만들고, 한 번의 루프에서 처리 */
import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int cnt = 1;
        int maxDay = (int) Math.ceil((100.0-progresses[0])/speeds[0]);
        for(int i=1; i<progresses.length; i++){
            int day = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);

            if(day <= maxDay){
                cnt++;
            } else {
                answer.add(cnt);
                cnt = 1;
                maxDay = day;
            }
        }
        answer.add(cnt);
        return answer.stream().mapToInt(i->i).toArray();
    }
}   
// 다른 사람 풀이
// 배포는 앞 작업이 끝나야 가능하다는 조건을 day를 증가시키면서 자연스럽게 처리하는 방식
import java.util.Arrays;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] dayOfend = new int[100]; // 각 일차에 몇 개의 기능이 배포되는가 (작업 개수는 최대 100개)
        int day = 0;
        for(int i=0; i<progresses.length; i++) {
            while(progresses[i] + (day*speeds[i]) < 100) {
                day++;
            }
            dayOfend[day]++;
        }
        return Arrays.stream(dayOfend).filter(i -> i!=0).toArray();
    }
}