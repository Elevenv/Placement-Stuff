// https://www.codechef.com/problems/RPD

import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int t;
		Scanner sc = new Scanner(System.in);
		t = sc.nextInt();
		while(t-->0){
		    int n = sc.nextInt();
		    int arr[] = new int[n];
		    for(int i=0;i<n;i++){
		        arr[i] = sc.nextInt();
		    }
		    int max = 0;
		    
		    for(int i=0;i<n;i++){
		        for(int j=0;j<n;j++){
		            if(i!=j){
		                int num = arr[i]*arr[j];
    		            int add = 0;
    		            int rem = 0;
    		            while(num>0){
    		                rem = num%10;
    		                add+=rem;
    		                num/=10;
    		            }
    		            if(add>max)
    		                max = add;
		            }
		        }
		    }
		    System.out.println(max);
		}
	}
}
