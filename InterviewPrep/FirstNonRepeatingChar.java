import java.util.HashMap;

public class FirstNonRepeatingChar {
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        pf(nonRepeating("abcab")); // should return 'c'
        pf(nonRepeating("abab")); // should return null
        pf(nonRepeating("aabbbc")); // should return 'c'
        pf(nonRepeating("aabbdbc")); // should return 'd'
    }

    public static void pf(Object x) {
        System.out.println(x);
    }

    // Implement your solution below.
    public static Character nonRepeating(String s) {
        if (s == null) {
            return null;
        }
        if (s.length() == 0) {
            return null;
        }
        if (s.length() == 1) {
            return s.charAt(0);
        }
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        for (Character c: s.toCharArray()) {
            if (hm.keySet().contains(c)) {
                int i = hm.get(c);
                hm.remove(c);
                hm.put(c, i + 1);
            } else {
                hm.put(c, 1);
            }
        }
        for (Character c: s.toCharArray()) {
            if (hm.get(c) == 1) {
                return c;
            }
        }
        return null;
    }
}

