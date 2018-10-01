import java.util.*;



public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int numero,fibo1,fibo2,i;
        numero = 500
	while(numero<=1);
        fibo1=1;
        fibo2=1;
        System.out.print(fibo1 + " ");
        for(i=2;i<=numero;i++){
             System.out.println(fibo2);
             fibo2 = fibo1 + fibo2;
             fibo1 = fibo2 - fibo1;
        }
    }
}