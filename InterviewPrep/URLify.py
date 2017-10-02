# URLify a given string: Replace all spaces with %20. Assume there is enough space in the end.
# Ex: "Mr. John Smith    " --> "Mr.%20John%20Smith"



def main():
    str = "Mr. John Smith    "
    str_l = list(str)

    # The count variable starts from the last non-space char
    # The i variable starts from the end.
    # When a space char is not encountered, str_l[count] is copied into str_l[i]
    # When a space char is encountered, str_l[i-2] to str_l[i] gets '%20'

    count = len(str_l) - 1
    i = len(str_l) - 1
    while str_l[count] == ' ':
        count -= 1

    while i > 1:
        if str_l[count] == ' ':
            str_l[i] = '0'
            str_l[i-1] = '2'
            str_l[i-2] = '%'
            i -= 2
        else:
            str_l[i] = str_l[count]
        count -= 1
        i -= 1
    print ''.join(str_l)


if __name__ == "__main__":
    main()



