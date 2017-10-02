# Count how many pairs add up to a target sum.
# WRONG CODE: MUST FIX.

'''
Test case format:
First line, number of test cases, N.
N pairs of lines: 1st of them: <length of array> <target sum>
                  2nd of them: the list separated by spaces.

4
4 6
1 5 7 -1
4 2
1 1 1 1
5 6
1 5 7 -1 5
13 11
10 12 10 15 -1 7 6 5 4 2 1 1 1
'''

'''
Examples:
Input  :  arr[] = {1, 5, 7, -1},
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  arr[] = {1, 5, 7, -1, 5},
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)

Input  :  arr[] = {1, 1, 1, 1},
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6,
                   5, 4, 2, 1, 1, 1},
          sum = 11
Output :  9
'''


def main():
    N = input()
    test_cases = []
    for i in range(N):
        firstline = raw_input()
        sum = firstline.split()[1]
        arr = []
        list_ip = raw_input()
        for j in range(int(firstline.split()[0])):
            arr.append(int(list_ip.split()[j]))
        to_append = (sum, arr)
        test_cases.append(to_append)
    for i in test_cases:
        print num_elts_target_sum(i)

def num_elts_target_sum(target_and_list):
    target = int(target_and_list[0])
    l = target_and_list[1]
    num_elts = 0
    # Create a dictionary that has the counts of each number - O(n)
    # Go through each element, check if target - element is there. Decrement count, add to num_elts
    m = {}
    for i in l:
        if i not in m.keys():
            m[i] = 1
        else:
            m[i] += 1
    print "M:", m
    for i in l:
        if m.get(target - i) is not None:
            num_elts += 1
            if (target - i) == i:
                m[target - i] -= 1
    return num_elts/2

if __name__ == "__main__":
    main()