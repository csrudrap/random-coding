# Given 2 arrays, return an array of all the common elements.

# Hint: Similar approach to merge of mergesort. 

def common_elements(A, B):
    # A: 1,3,4,6,7,9
    # B: 1,2,4,5,9,10
    # i and j are variables that will be used to loop through A and B respectively.
    # If A[i] = B[j], add to common_arr and increment i and j.
    # Else, see if A[i] > B[j]. If this is true, the B[i] value can't be found in A[i:].
    # So, if A[i] < B[j], increment i and check again. Otherwise, increment j and check again.

    common_arr = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            common_arr.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return common_arr

# Note: If '[' and ']' are not put in the below line and only comma separated values are given, A becomes a tuple.
A = [1,3,4,6,7,9]
B = [1,2,4,5,9,10]
print common_elements(A, B)

A = [1,4,5,11,15,18,22,23,27,30]
B = [2,3,5,6,7,9,11,13,14,16,19,22,26,28,30,38]
print common_elements(A, B)


