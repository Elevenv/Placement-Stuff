//CodeChef Problem

import java.util.*;

class StudyingAlp{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String canRead = sc.next();
        int n = sc.nextInt();
        int count;
        for(int i=0;i<n;i++){
            count = 0;
            String chkString = sc.next();
            for(int j=0;j<canRead.length();j++){
                for(int k=0;k<chkString.length();k++){
                    if(chkString.charAt(k)==canRead.charAt(j)){
                        count++;
                    }
                }
            }
            if(count==chkString.length())
                System.out.println("Yes");
            else
                System.out.println("No");
        }
    }
}