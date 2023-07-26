import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static void isPrime(int m)
        {
            int flag=0,i;
            int n=m;
            if(n==0||n==1)
               System.out.println("COMPOSITE");
               if(n==2)
               System.out.println("PRIME");
            else{  
                for(i=2;i<m;i++){      
                    if(n%i==0){      
                        System.out.println("COMPOSITE");      
                        flag=1;      
                        break;      
                    }      
                }      
                if(flag==0)  {
                     System.out.println("PRIME"); 
                     }  
            }
        }
        
        static void isOdd(int m)
        {
            if(m%2==0)
            {
                System.out.println("EVEN");
            }
            else
            {
                System.out.println("ODD");
            }
        }
        
        static void isPalindrome(int n)
        {
            if(Integer.toString(n).equals( new StringBuilder(Integer.toString(n)).reverse().toString()))
 
   System.out.println("PALINDROME");    
  else    
   System.out.println("NOT PALINDROME");    
        }

    public static void main(String[] args) {
        int i,j;
        
        
        
        Scanner scanner=new Scanner(System.in);
        int numOfTestCases=scanner.nextInt();
        int array[][]=new int[numOfTestCases][2];
        for(i=0;i<numOfTestCases;i++)
        {
            for(j=0;j<2;j++)
            {
                array[i][j]=scanner.nextInt();
            }
        }
        for(i=0;i<numOfTestCases;i++)
        {
            if(array[i][0]==1)
            {
               isOdd(array[i][1]); 
            }
            if(array[i][0]==2)
            {
               isPrime(array[i][1]); 
            }
            if(array[i][0]==3)
            {
               isPalindrome(array[i][1]); 
            }
        }
        
    }
}
