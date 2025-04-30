import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        // 1. int[] -> String[]로 변환
        String[] strNums = Arrays.stream(numbers)   // IntStream
                .mapToObj(String::valueOf)          // Stream<String>
                .toArray(String[]::new);            // String[]

        // 2. 커스텀 Comparator로 정렬 (내림차순 정렬)
        Arrays.sort(strNums, (a, b)->(b+a).compareTo(a+b));

        return strNums[0].equals("0") ? "0" : String.join("", strNums);
    }
}

/*
int[] 같은 기본형 배열은 객체가 아니기 때문에, .stream()이 아닌 Arrays.stream(arr)로 IntStream을 만든 다음
객체 스트림으로 바꿀 때 .mapToObj()를 사용

String::valueOf는 i -> String.valueOf(i)의 메서드 레퍼런스 버전
String[]::new는 size -> new String[size]를 줄여 쓴 배열 생성자 참조
 */