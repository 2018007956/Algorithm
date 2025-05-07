class Solution {
    static int[] arr;
    static int goal;
    static int answer;

    public int solution(int[] numbers, int target) {
        arr = numbers;
        goal = target;
        dfs(0, 0);
        return answer;
    }

    private static void dfs(int depth, int sum) {
        if(depth==arr.length) {
            if(sum==goal) answer++;
            return;
        }
        dfs(depth+1, sum+arr[depth]);
        dfs(depth+1, sum-arr[depth]);
    }
}