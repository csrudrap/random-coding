import java.util.*;

public class PermOfPalindrome {
/*
 Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards 
and backwards. A permutation is a rearrangement of letters. The palindrome 
does not need to be limited to just dictionary words.
 */
	
	public static void main(String[] args) {
		String s1 = "tactcoapapa";
		String s2 = "Tact Coa";
		System.out.println(isPermOfPalindrome(s1.toLowerCase()));
		System.out.println(isPermOfPalindrome(s2.toLowerCase()));
	}

	private static boolean isPermOfPalindrome(String s) {
		Map<Character, Integer> hm = new HashMap<Character, Integer>();
		char[] cArr = s.toCharArray();
		for (char c: cArr) {
			if (hm.get(c) == null) {
				// Let's only consider lowercase letters of the Alphabet.
				if ('a' <= c && c <= 'z') {
					hm.put(c, 1);
				}
			} else {
				hm.put(c, hm.get(c) + 1);
			}
		}
		int oddCharCount = 0;
		for (char c: hm.keySet()) {
			if (hm.get(c) % 2 == 1) {
				oddCharCount++;
			}
		}
		if (oddCharCount > 1) {
			// More than one character has an odd count in the string.
			// At most one character can have an odd count for a palindrome. 
			return false;
		}
		// At most one character has an odd count now. 
		// Other characters with even counts can be split such that half of
		// them are on the left side and half of them are on the right side.
		return true;
	}
}
