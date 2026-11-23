import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int square = N * N;
        System.out.println(square);
        if (N < 5){
            System.out.print("tiny");
        }
    }
}