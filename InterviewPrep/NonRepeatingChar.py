# Given a string, return a non-repeating character.
def non_repeating(given_string):
    d = {}
    for ch in given_string:
        if ch not in d.keys():
            d[ch] = 1
        else:
            d[ch] += 1
    for i in d.keys():
        if d[i] == 1:
            return i
    return None

# NOTE: The following input values will be used for testing your solution.
print non_repeating("abcab") # should return 'c'
print non_repeating("abab") # should return None
print non_repeating("aabbbc") # should return 'c'
print non_repeating("aabbdbc") # should return 'd' or 'c'
