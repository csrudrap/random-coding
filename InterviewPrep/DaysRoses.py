'''
Google coding test question:

Given P = [2, 5, 1, 4, 3] (meaning that the 2nd rose blooms on Day1, 5th rose on Day2, 1st rose on Day3, 4th rose on
Day4, 3rd rose on Day5), and K = 2, the function should return 2, because that is the earliest K-empty (2-empty) day.

A K-empty day is a day where there are one or more occurrences of precisely K consecutive roses that have not bloomed
yet. Here, on the 1st day, the 2nd rose blooms. So there is a 4-empty group but no 2-empty groups.
On the 2nd day, the 5th rose blooms. 3rd and 4th roses have not bloomed, so this forms a 2-empty group.
On the 3rd day, the 1st rose blooms. 3rd and 4th roses have not bloomed, so this forms a 2-empty group.

But the 2nd day is chosen as the answer because it occurs before the 3rd day.

Requirement: Solution in n*log(n)
'''

# n^2 approach:
import re
def continuous_zeroes(bit_arr, K):
    # Something like 10011, K = 2
    # And with       11111 = 10011
    str_arr = map(str, bit_arr)
    str_str = ''.join(str_arr)
    str_zeroes = '0' * K
    to_cmp = re.compile(r"""(1{0}1|1{0}$|^{0}1)""".format(str_zeroes))
    return to_cmp.search(str_str) is not None


def solution(P, K):
    # write your code in Python 2.7
    # Have a bit array. Create it for each day.
    # Check if K-empty group is possible. Return i+1.

    bit_arr = [0] * len(P)
    # Say P = [2,5,1,4,3], K=2
    # (i-1)th position in the bit_arr should be set to 1.
    for i in range(len(P)):
        bit_arr[P[i] - 1] = 1
        if continuous_zeroes(bit_arr, K):
            return i + 1
    return -1

def main():
    print solution([2,5,1,4,3], 2)
    print solution([2,4,3,1,5], 2)


if __name__ == "__main__":
    main()
