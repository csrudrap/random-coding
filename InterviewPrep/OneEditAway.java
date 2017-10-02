import java.util.*;
public class OneEditAway {
	/*
	There are three types of edits that can be performed on strings: insert 
	a character, remove a character, or replace a character. Given two 
 	strings, write a function to check if they are one edit 
 	(or zero edits) away. 
	
	EXAMPLE
	pale, ple -> true
	pales, pale -> true
	pale, bale -> true
	pale, bae -> false
	apple, aple -> true
	*/
	
	public static void main(String[] args) {
		String[][] strings = {{"pale", "bale"}, {"pales", "pale"}, 
				{"pale", "ple"}, {"pale", "bae"}, {"apple", "aple"}, 
				{"aaaaa", "aaa"}, {"", "s"}, {"a", "ab"}, {"a", "ba"}, {"a", "bc"}};
		for (String[] s: strings) {
			System.out.println(isOneEditAway(s[0], s[1]));
		}
	}

	private static boolean isOneEditAway(String s1, String s2) {
		// Inserting a character in one string to make it the other string
		// is the same as removing it from the other, so they are equivalent.
		// Two methods: isOneReplaceAway and isOneInsertAway.
		// For isOneDeleteAway, just pass s2, s1 to isOneInsertAway
		if (s1.length() == s2.length()) {
			return isOneReplaceAway(s1, s2);
		} else if (s1.length() + 1 == s2.length()) {
			return isOneInsertAway(s1, s2);
		} else if (s1.length() - 1 == s2.length()) {
			return isOneInsertAway(s2, s1);
		} else {
			return false;
		}
	}

	private static boolean isOneInsertAway(String s1, String s2) {
		// Length of s1 MUST now be one less than the length of s2.
		// Handle cases when s1.length() is 0 or 1 first.
		if (s1.length() == 0) {
			// For example: "", "s"
			return true;
		} else if (s1.length() == 1) {
			// Three conditions: 1st letter matches, 2nd letter matches, no match
			if (s1.charAt(0) == s2.charAt(0) || s1.charAt(0) == s2.charAt(1)) {
				return true;
			} else {
				return false;
			}
		}
		boolean oneCharAway = false;
		int indexS1 = 0;
		int indexS2 = 0;
		while (indexS1 < s1.length() && indexS2 < s2.length()) {
			if (s1.charAt(indexS1) != s2.charAt(indexS2)) {
				// This may be the point of addition of one char.
				// Increment the index of the bigger string once.
				// The rest of the two strings should match.
				// For ex: aple and apple. After "ap", the first mismatch
				// occurs. Increment indexS2 to point to the second p.
				// From here, "le" will be the same for both. The boolean
				// oneCharAway can be set only once.
				if (oneCharAway == true) {
					return false;
				}
				indexS2++;
				oneCharAway = true;
			}
			indexS1++;
			indexS2++;
		}
		return true;
	}

	private static boolean isOneReplaceAway(String s1, String s2) {
		boolean oneCharMismatch = false;
		for (int index = 0; index < s1.length(); index++) {
			if (s1.charAt(index) != s2.charAt(index)) {
				if (oneCharMismatch == false) {
					// Make sure this happens only once by setting the boolean to true.
					oneCharMismatch = true;
				} else {
					return false;
				}
			}
		}
		return oneCharMismatch;
	}
}
