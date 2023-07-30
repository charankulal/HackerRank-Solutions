// Question Link : https://www.hackerrank.com/challenges/java-primality-test/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      BigInteger n = in.nextBigInteger();
      in.close();
      System.out.println( n.isProbablePrime(1000) ? "prime" : "not prime" );
   }
}
