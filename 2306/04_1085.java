import java.util.Scanner;
 
public class test {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int x;
        int y;
        int w;
        int h;
        int num1;
        int num2;
        int num3;
        int num4;
        x = sc.nextInt();
        y = sc.nextInt();
        w = sc.nextInt();
        h = sc.nextInt();
        num1 = w - x;
        num2 = h - y;
        num3 = x;
        num4 = y;
        if (num1 < num2 && num1 < num3 && num1 < num4){
            System.out.print(num1);
        }else if (num2 < num1 && num2 < num3 && num2 < num4){
            System.out.print(num2);
        }else if (num3 < num1 && num3 < num2 && num3 < num4){
            System.out.print(num3);
        }else {
            System.out.print(num4);
        }
    }
}
