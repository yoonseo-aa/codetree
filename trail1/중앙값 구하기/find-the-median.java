import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        int mid;

        if (a >= b) {
            if (b >= c) {
                mid = b;       
            } else if (a >= c) {
                mid = c;       
            } else {
                mid = a;       // c > a >= b
            }
        } else {
            if (a >= c) {
                mid = a;       // b > a >= c
            } else if (b >= c) {
                mid = c;       // b >= c > a
            } else {
                mid = b;       // c > b > a
            }
        }

        System.out.print(mid);
    }
}