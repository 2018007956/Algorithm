import java.util.*;
class Solution {
    int answer = (int)1e9;
    boolean[] visited = new boolean[50];
    public boolean check(String a, String b) {
        int cnt = 0;
        for(int i=0; i<a.length(); i++) {
            if(a.charAt(i)!=b.charAt(i)) cnt++;
        }

        if(cnt==1) return true;
        else return false;
    }
    public void dfs(int cur, int cnt, String target, String[] words) {
        if(words[cur].equals(target)) {
            answer = Math.min(answer, cnt);
            return;
        }

        visited[cur] = true;
        for(int i=0; i<words.length; i++) {
            if(!visited[i] && check(words[cur], words[i])) {
                dfs(i, cnt+1, target, words);
            }
        }
    }
    public int solution(String begin, String target, String[] words) {
        for(int i=0; i<words.length; i++) {
            if(check(begin, words[i])) {
                visited[i] = true;
                dfs(i, 1, target, words);
                visited[i] = false;
            }
        }
        return answer==1e9? 0 : answer;
    }
}

/*
if(words[cur]==target)
    ==는 객체의 주소 비교이므로 문자열 비교에 적절하지 않음
    내용 비교를 해야 하므로 equals()를 써야 함
 */

// 다른 사람 풀이
import java.util.*;
class Solution {
    
    class Word {
        String word;
        int depth;
        
        Word(String word, int depth) {
            this.word = word;
            this.depth = depth;
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        boolean[] visited = new boolean[words.length];
        Queue<Word> queue = new LinkedList<>();
        
        queue.offer(new Word(begin, 0));
        
        while(!queue.isEmpty()) {
            Word current = queue.poll();
            
            if(current.word.equals(target)) {
                return current.depth;
            }
            
            for(int i = 0; i < words.length; i++) {
                if(!visited[i] && isOneDiff(current.word, words[i])) {
                    visited[i] = true;
                    queue.offer(new Word(words[i], current.depth + 1));
                }
            }
        }
        return 0;
    }
    
    private boolean isOneDiff(String a, String b) {
        int diff = 0;
        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) != b.charAt(i)) diff++;
        }
        return diff == 1;
    }
}