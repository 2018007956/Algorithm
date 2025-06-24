import java.util.Arrays;
class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for(int i=0; i<phone_book.length-1; i++){
            if(phone_book[i+1].startsWith(phone_book[i])) { return false; }
        }
        return true;
    }
}

// 다른 풀이
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>(Arrays.asList(phone_book));

        for(String str : set) {
            for(int i=1; i<str.length(); i++) {
                if(set.contains(str.substring(0, i))) { return false; }
            }
        }

        return true;
    }
}
/* 아래 코드는 모두 같은 동작 수행
HashSet<String> set = new HashSet<>(Arrays.asList(phone_book));
---
HashSet<String> set = new HashSet<>();
Arrays.stream(phone_book).forEach(s->set.add(s));
---
HashSet<String> set = new HashSet<>();
Collections.addAll(set, phone_book);
---
HashSet<String> set = new HashSet<>();
for(String s : phone_book) {
    set.add(s);
}
 */