# Given a string, return the first non-repeating character.
def non_repeating(given_string):
    # Create a list of 26 characters, assuming the small letters of the English alphabet.
    l = [0] * 26
    for ch in given_string:
        l[ord(ch) - 97] += 1
    for ch in given_string:
        if l[ord(ch) - 97] == 1:
            return ch
    return None
              
# NOTE: The following input values will be used for testing your solution.
print non_repeating("abcab") # should return 'c'
print non_repeating("abab") # should return None
print non_repeating("aabbbc") # should return 'c'
print non_repeating("aabbdbc") # should return 'd'
