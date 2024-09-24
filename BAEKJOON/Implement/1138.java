import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int[] arr = new int[N+1];
        List<Integer> result = new ArrayList<>();

        for(int i=1; i<=N; i++) {
            arr[i] = scan.nextInt();
        }

        for(int i=N; i>=1; i--) {
            result.add(arr[i], i);
        }

        for(int k:result) {
            System.out.print(k+" ");
        }

        scan.close();
    }    
}