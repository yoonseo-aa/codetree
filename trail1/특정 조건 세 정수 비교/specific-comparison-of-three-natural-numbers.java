import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        
        if(a<=b && a <= c){
            System.out.print(1);
        }else{
             System.out.print(0);
        }
        if(a == b && b == c && c == a){
            System.out.print(" 1");
        }else{
            System.out.print(" 0");
        }
    }
}