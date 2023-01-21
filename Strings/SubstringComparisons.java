import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int k=sc.nextInt();
        String c=null;
        String minimum = s.substring(0,k);
        String maximum = s.substring(0,k);
        for (int i = 1; i<=s.length()-k; i++){
            c=s.substring(i,i+k);
            if(c.compareTo(minimum) < 0)
                minimum=c;
            else if(c.compareTo(maximum)>0)
                maximum=c;
        }        
        System.out.println(minimum);
        System.out.println(maximum);
    }
}
