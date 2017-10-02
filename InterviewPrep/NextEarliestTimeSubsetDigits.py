# Google coding test question
'''

Given a non-empty string S in "HH:MM" format representing the current time on your watch, return string T specifying
the first time after the current minute that can be represented by a subset of the digits of S (not all digits of S
have to be used).
Ex: "11:00" should return "11:01"
    "06:59" should return "09:00"
    "23:59" should return "22:22" (next day!)
The string is a valid time from "00:00" to "23:59"
The focus is on correctness and not on performance.

'''
import itertools
import re

def is_valid_time(s):
    s = ''.join(s)
    minutes = s[2:]
    hours = s[:2]
    hourmatch = re.match("([0-1][0-9]|[2][0-3])", hours)
    minmatch = re.match("[0-5][0-9]", minutes)
    return hourmatch is not None and minmatch is not None


def solution(S):
    # write your code in Python 2.7
    # Given HH:MM as 15:35, 15:51 is the answer
    str_without_colon = ''.join(S.split(':'))
    set_str = set(str_without_colon)
    l = list(set_str)
    # Generate every combination possible, including duplicates, as efficiency doesn't matter.
    i = itertools.product(l, repeat=4)
    list_of_times = []
    for j in i:
        # Check if this is a valid time.
        if is_valid_time(list(j)):
            # Append only valid times to list_of_times.
            list_of_times.append(''.join(list(j)))
    list_of_times = sorted(list_of_times)
    # If there can be greater times, get a list of all the greater times.
    greater_times = [i for i in list_of_times if i > str_without_colon]
    if greater_times is None:
        greater_times = []

    if len(greater_times) > 0:
        # There are greater times, so get the smallest greater time.
        l_ret = list(sorted(greater_times)[0])
        l_ret.append('0')
        l_ret[4] = l_ret[3]
        l_ret[3] = l_ret[2]
        l_ret[2] = ':'
        return ''.join(l_ret)
    else:
        # There are no greater times. So choose the smallest time.
        # This will be from the next day.
        l_ret = list(list_of_times[0])
        l_ret.append('0')
        l_ret[4] = l_ret[3]
        l_ret[3] = l_ret[2]
        l_ret[2] = ':'
        return ''.join(l_ret)


def main():
    print "23:56\t", solution("23:56")
    print "23:59\t", solution("23:59")
    print "11:00\t", solution("11:00")
    print "11:59\t", solution("11:59")
    print "00:00\t", solution("00:00")
    print "06:59\t", solution("06:59")
    print "15:35\t", solution("15:35")

if __name__ == "__main__":
    main()