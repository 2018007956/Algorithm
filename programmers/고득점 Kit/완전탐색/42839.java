import java.util.*;
class Solution {
    Set<Integer> set = new HashSet<>();

    public int solution(String numbers) {
        for(int i=1; i<=numbers.length(); i++) {
            permutation(numbers, "", new boolean[numbers.length()], i);
        }

        int cnt = 0;
        for(int x : set) {
            if(isPrimeNum(x)) cnt++;
        }
        return cnt;
    }

    public void permutation(String str, String temp, boolean[] visited, int length) {
        if(temp.length()==length) {
            set.add(Integer.parseInt(temp));
            return;
        }
        for(int i=0; i<str.length(); i++) {
            if(!visited[i]) {
                visited[i] = true;
                permutation(str, temp+str.charAt(i), visited, length);
                visited[i] = false;
            }
        }
    }

    public boolean isPrimeNum(int x) {
        if(x<2) return false;
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) return false;
        }
        return true;
    }
}