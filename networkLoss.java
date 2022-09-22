import java.util.*;
class networkLoss{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();

        int init=0;
        int t = 0;
        char c1,c2;

        int i;
        for(i=0;i<s2.length();i++){
            c2 = s2.charAt(i);
            t = i+init;
            c1 = s1.charAt(t);
            // System.out.println();          
         
        if(c2!=c1){
                System.out.println(c1);
                init++;
            }
        }
        if(i+init<s1.length()){
            for(int j=i;j<s1.length();j++){
                System.out.println(s1.charAt(j+init));
            }
        }
    }
}