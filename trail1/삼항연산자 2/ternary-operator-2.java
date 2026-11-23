import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        char result;
        result = a == 1 ? 't' : 'f';
        System.out.print(result);
    }
}