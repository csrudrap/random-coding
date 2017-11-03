# URLify a given string. Assume there is enough place in the end of the string.
# For "Mr John Smith    ", 13: where 13 is the true length, return:
#     "Mr%20John%20Smith"

def urlify(s, l):
    # start fin_index from len(s)-1 backwards
    # start str_index from l-1 backwards.
    if len(s) == 0:
        return s
    s_list = list(s)
    fin_index = len(s) - 1
    str_index = l - 1
    while str_index >= 0 and fin_index >= 0:
        if s_list[str_index] == ' ':
            s_list[fin_index] = '0'
            s_list[fin_index - 1] = '2'
            s_list[fin_index - 2] = '%'
            fin_index -= 3
            str_index -= 1
        else:
            s_list[fin_index] = s_list[str_index]
            fin_index -= 1
            str_index -= 1
    return ''.join(s_list)

print urlify("Mr John Smith    ", 13) # Should print "Mr%20John%20Smith"
print urlify("Nospace", 7) # Should print Nospace
print urlify("", 0) # Should print nothing.
print urlify("   ", 1) # Should print %20
print urlify("The code is so buggy and full of errors                ", 39) # Should print The%20code%20is%20so%20buggy%20and%20full%20of%20errors


