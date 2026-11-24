import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int middle = sc.nextInt(),fin = sc.nextInt();
        if(middle < 90){
            System.out.print(0);
        }else if(fin >= 95){
            System.out.print(100000);
        }else if(fin >= 90) {
            System.out.print(50000);
        }else{
            System.out.print(0);
        }
    }
}