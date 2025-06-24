import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0; i<clothes.length; i++) {
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0) + 1);
        }
        
        int answer = 1;
        for(int n : map.values()) {
            answer *= n+1;
        }
        
        return answer-1;
    }
}

// 다른 사람 풀이
import java.util.*;
import static java.util.stream.Collectors.*; // Collectors 클래스의 정적 메서드들을 사용하기 위해 선언
class Solution {
    public int solution(String[][] clothes) {
        return Arrays.stream(clothes)
                .collect(
                    groupingBy( // 1. 옷 종류별로 그룹핑
                        p -> p[1],  // -> 옷의 종류 (ex. "headgear")
                        mapping(p -> p[0], counting()) // -> 옷 이름을 모아서 개수 세기 (counting()은 Long 반환)
                    )
                ) 
                .values() // 2. Map<String, Long>의 value만 가져오기 (각 종류별 개수)
                .stream()
                .collect(
                    reducing(1L, (x, y) -> x * (y + 1)) // 스트림 요소들이 Long 타입이므로 초기값을 1L(long타입)으로 설정
                ).intValue() - 1;
    }
}