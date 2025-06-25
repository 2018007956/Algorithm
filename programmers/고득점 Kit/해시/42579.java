import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, List<int[]>> map = new HashMap<>();
        HashMap<String, Integer> mapSum = new HashMap<>();
        for(int i=0; i<genres.length; i++) {
            map.computeIfAbsent(genres[i], k -> new ArrayList<>())
                .add(new int[]{plays[i], i});
            mapSum.put(genres[i], mapSum.getOrDefault(genres[i],0)+plays[i]);
        }
        
        // 1. 속한 노래가 많이 재생된 장르
        List<String> sortedList = new ArrayList<>(mapSum.keySet());
        sortedList.sort((a, b) -> mapSum.get(b).compareTo(mapSum.get(a)));
        
        List<Integer> answerList = new ArrayList<>();
        for(String key : sortedList) {
            // 2. 장르 내에서 많이 재생된 노래
            List<int[]> songs = map.get(key);
            songs.sort((a, b) -> {
                if (b[0] != a[0]) return b[0] - a[0];   // 재생 수 기준 내림차순
                return a[1] - b[1];                     // 재생 수 같으면 인덱스 오름차순
            });
                
            // for (int[] arr : songs) {
            //     System.out.println(key + " = " +Arrays.toString(arr));
            // }
            for (int i=0; i<Math.min(2, songs.size()); i++) {
                answerList.add(songs.get(i)[1]);
            }
        }
        
        int[] answer = new int[answerList.size()];
        for(int i=0; i<answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}
/*
b[0] - a[0] 과 같은 Comparator 표현식이 내림차순 정렬을 나타내는 이유
Comparator<T> comp = (a, b) -> {
    if (a < b) return -1;   // 리턴값이 음수면 a가 먼저 (오름차순)
    if (a > b) return 1;    // 리턴값이 양수면 b가 먼저
    return 0;               // 같음. 순서 유지
}

3과 5를 비교한다고 가정하면,

① 오름차순 정렬: (a, b) -> a - b
a	b	a - b	의미
3	5	-2	3이 먼저 → 오름차순
5	2	3	2가 먼저 → 오름차순
-> 작은 값이 먼저 오도록 유도함

② 내림차순 정렬: (a, b) -> b - a
a	b	b - a	의미
3	5	2	5가 먼저 → 내림차순
5	2	-3	5가 먼저 → 내림차순
-> 큰 값이 먼저 오도록 유도함
*/

// 다른 사람 풀이
import java.util.*;
public class Solution {
    public class Music implements Comparable<Music>{
        private int played;
        private int id;
        private String genre;
        public Music(String genre, int played, int id) {
            this.genre = genre;
            this.played = played;
            this.id = id;
        }

        @Override
        public int compareTo(Music other) {
            if (this.played == oter.played) return this.id - other.id; // 고유 번호 작은 순
            return other.played - this.played; // 재생 수 높은 순서
        }

        public String getGenre() { return genre; }
    }

    public int[] solution(String[] genres, int[] plays) {
        return IntStream.range(0, genres.length)
            .mapToObj(i -> new Music(genres[i], plays[i], i))
            .collect(Collectors.groupingBy(Music::getGenre))            // Map<장르, 음악들>
            .entrySet().stream()                                        // Map을 key-value 쌍으로 순회
            .sorted((a, b) -> sum(b.getValue()) - sum(a.getValue()))    // 장르별 총 재생수로 내림차순 정렬
            .flatMap(x -> x.getValue().stream().sorted().limit(2))      // 각 장르에서 상위 2개 곡 뽑음
            .mapToInt(x -> x.id).toArray();
    }

    private int sum(List<Music> value) {
        int answer = 0;
        for (Music music : value) {
            answer += music.played;
        }
        return answer;
    }
}