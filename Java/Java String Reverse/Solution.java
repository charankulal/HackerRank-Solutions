import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B="";
        char ch;
        for (int i=0; i<A.length(); i++)
      {
        ch= A.charAt(i); 
        B= ch+B;
      }
        if(A.equals(B))
        {
            System.out.println("Yes");
        }
        else
         System.out.println("No");
    }
}
