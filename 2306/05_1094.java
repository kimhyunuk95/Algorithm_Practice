import java.util.Scanner;

public class Baekjoon_1094 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n,cnt=0;
        n = sc.nextInt();
        while(n>0){
            if (n%2 == 1){
                cnt++;
            }
            n /= 2;
        }
        System.out.print(cnt);
    }
}

// 2진수로 나타내어 1이 몇개인지 찾아내는 문제이다. 
