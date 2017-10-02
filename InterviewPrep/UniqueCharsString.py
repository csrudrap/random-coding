# Check if a string has unique characters:

def isUniq(s):
    s_set = set()
    for i in s:
        if i not in s_set:
            s_set.add(i)
        else:
            return False
    return True

def main():
    s1 = "abcdefgh"
    s2 = "abagghscwfgfddd"
    s3 = "ufyaeisfsd"
    s4 = "pqowrocnv"
    b1 = isUniq(s1)
    b2 = isUniq(s2)
    b3 = isUniq(s3)
    b4 = isUniq(s4)

    print s1,":",b1
    print s2,":",b2
    print s3,":",b3
    print s4,":",b4

if __name__ == '__main__':
    main()