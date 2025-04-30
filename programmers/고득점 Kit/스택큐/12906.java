import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] temp = new int[arr.length];
        int idx = 0;
        temp[idx++] = arr[0];
        for(int i=1; i<arr.length; i++) {
            if(arr[i] != arr[i-1]) temp[idx++] = arr[i];
        }

        int[] answer = new int[idx];
        System.arraycopy(temp, 0, answer, 0, idx);
        return answer;
    }
}

// 다른 풀이
public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> tempList = new ArrayList<Integer>();
        int preNum = 10;
        for(int num : arr) {
            if(preNum != num)
                tempList.add(num);
            preNum = num;
        }
        int[] answer = new int[tempList.size()];
        for(int i=0; i<answer.length; i++) {
            answer[i] = tempList.get(i).intValue();
        }
        return answer;
    }
}