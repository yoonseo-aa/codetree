import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char symptom1 = sc.next().charAt(0);
        int tem1 = sc.nextInt();
        char symptom2 = sc.next().charAt(0);
        int tem2 = sc.nextInt();
        char symptom3 = sc.next().charAt(0);
        int tem3 = sc.nextInt();
        int cnt = 0;

        if(symptom1 == 'Y'){
            cnt = tem1 >= 37 ? cnt + 1 : cnt;
        } 
        if(symptom2 == 'Y'){
            cnt = tem2 >= 37 ? cnt + 1 : cnt;
        }
        if(symptom3 == 'Y'){
            cnt = tem3 >= 37 ? cnt + 1 : cnt;
        }

        if(cnt >= 2){
            System.out.print('E');
        }else{
            System.out.print('N');
        }


    }
}