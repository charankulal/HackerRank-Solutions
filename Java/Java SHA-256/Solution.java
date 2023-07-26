import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

public class Solution {
    
    public static String getHexString(String message)
    {
        try{
            MessageDigest messageDigest=MessageDigest.getInstance("SHA-256");
            byte[] hash=messageDigest.digest(message.getBytes(StandardCharsets.UTF_8));
            BigInteger number = new BigInteger(1, hash);
            StringBuilder hexString = new StringBuilder(number.toString(16));
            while (hexString.length() < 64)
        {
            hexString.insert(0, '0');
        }
 
        String Result= hexString.toString();
        
        return Result;
        }catch(NoSuchAlgorithmException e)
        {
            e.printStackTrace();
        }
        return "Result";
    }

    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        String message=scanner.nextLine();
        scanner.close();
        System.out.println(getHexString(message));
    }
}
