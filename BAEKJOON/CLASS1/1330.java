import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        in.close();

        String ret = (a>b) ? ">" : ((a<b) ? "<" : "==");
        System.out.println(ret);
    }
}