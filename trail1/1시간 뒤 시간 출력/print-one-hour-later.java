import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] strArr = s.split(":");
        int hour = Integer.parseInt(strArr[0]);
        System.out.printf("%d:%s",hour+1, strArr[1]);
    }
}