// https://www.codechef.com/problems/ERROR

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
    static boolean solve(String s,String sub){
        
		for(int i = 0;i<=s.length()-3;i++){
		    int j;
		    for(j=0;j<3;j++){
		        if(s.charAt(i+j)!=sub.charAt(j))
		            break;
		        if(j==2)
		            return true;
		        }
		    }
	    return false;
    }
    
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int t;
		Scanner sc = new Scanner(System.in);
		t = sc.nextInt();
		while(t-->0){
		    String s = sc.next();
		    char arr[] = s.toCharArray();
		    String sub = "101";
		    boolean ans = solve(s,sub);
		    String sub1 = "010";
		    if(!ans)
		        ans = solve(s,sub1);
		    
		    if(ans)
		        System.out.println("Good");
		    else
		        System.out.println("Bad");
		}
		    
	}
}
