import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        int flag=0;
        Scanner scanner = new Scanner(System.in);
        String A=scanner.nextLine();
        String B=scanner.nextLine();
        System.out.println(A.length()+B.length());

        if(A.compareTo(B)>0)
        {
            System.out.println("Yes");
        }
        else
        System.out.println("No");
        System.out.println(A.substring(0, 1).toUpperCase()+A.substring(1, A.length())+" "+B.substring(0, 1).toUpperCase()+B.substring(1, B.length()));
    }
}
