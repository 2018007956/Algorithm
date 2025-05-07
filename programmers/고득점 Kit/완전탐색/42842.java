class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow;
        for(int h=3; h<total; h++) {
            if(total%h==0) {
                int w = total/h;
                if((w-2)*(h-2) == yellow)
                    return new int[]{w, h};
            }
        }
        // 모든 경우를 확인했지만 조건을 만족하지 않을 경우
        // 컴파일러 오류 대비
        return new int[0];
    }
}