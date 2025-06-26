import java.util.Stack;
class Solution {
    boolean solution(String s) {
        Stack<Character> st = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                st.push('(');
            } else {
                if (st.isEmpty() || st.peek()!='(') {
                    return false;
                } else {
                    st.pop();
                }
            }
        }
        return st.isEmpty();
    }
}

// 다른 사람 풀이
class Solution {
    boolean solution(String s) {
        int cnt = 0;
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(') cnt++;
            else if (s.charAt(i) == ')') cnt--;

            if (cnt < 0) break;
        }
        return cnt == 0 ? true : false;
    }
}