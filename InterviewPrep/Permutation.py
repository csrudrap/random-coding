# Given two strings, tell if one is a permutation of the other.

# Approaches: Sort the strings and check if they are same: n lg n
#             Maintain an array of 52 characters (if only letters are used). Increment the index with one
#  String, decrement with another. Second approach:

def is_permutation(s1, s2):
    a = []
    for i in range(52):
        a.append(0)
    for i in s1:
        a[ord(i) - 71] += 1
    for i in s2:
        a[ord(i) - 71] -= 1
    for i in range(len(a)):
        if a[i] != 0:
            return False
    return True


def main():
    s1 = "dog"
    s2 = "god"
    b12 = is_permutation(s1, s2)

    s3 = "dog"
    s4 = "God"
    b34 = is_permutation(s3, s4)

    s5 = "abdcGw"
    s6 = "Gdbcwa"
    b56 = is_permutation(s5, s6)

    print b12, b34, b56
if __name__ == "__main__":
    main()