import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] strArr = s.split("-");
        int year = Integer.parseInt(strArr[2]);
        int day = Integer.parseInt(strArr[1]);
        int month = Integer.parseInt(strArr[0]);

        System.out.printf("%d.%d.%d", year, month, day);
    }
}