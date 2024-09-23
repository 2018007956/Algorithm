// Solved (16m)
package Algorithm.BAEKJOON.Implement;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        if ((N/3 + N%3) %2 == 1){
            System.out.println("SK");
        } else {
            System.out.println("CY");
        }
    }
}