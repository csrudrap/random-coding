import java.util.*;

// NOT WORKING!!!
class StringDashes {
    public static String solution(String S, int K) {
        // write your code in Java SE 8
        // Input: 2-4A0r7-4k; Output: 24A0-R74K for K = 4
        // Start from the end. Count num of non-dash chars.
        char[] SArr = S.toUpperCase().toCharArray();
        char temp = Character.MIN_VALUE;
        int countNonDash = SArr.length - 1;
        int localCount = 0;
        for (int i = SArr.length - 1; i >= 0; i--) {
            if (SArr[i] != '-') {
                if (localCount < K) {
                    if (temp != Character.MIN_VALUE) {
                        SArr[countNonDash] = temp;
                        countNonDash--;
                        if (i > 0 && SArr[i-1] != '-') {
                            temp = SArr[i];
                        } else {
                            temp = Character.MIN_VALUE;
                        }
                    }
                    else {
                        SArr[countNonDash] = SArr[i];
                        countNonDash--;
                    }
                    localCount++;
                } else {
                    temp = SArr[i];
                    SArr[i] = '-';
                    localCount = 0;
                    countNonDash--;
                }
            } 
        }
        return new String(SArr);    
    }
    
    public static void main(String[] args) {
    		System.out.println(solution("2-4A0r7-4k", 4));
    }
}