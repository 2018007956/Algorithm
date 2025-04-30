import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        in.close();

        StringTokenizer st = new StringTokenizer(s, " ");
        System.out.println(st.countTokens());
    }
}