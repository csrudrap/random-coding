# Given an array like [3,4,-2,5,6], return 2 elements whose product is 20.

def find_product_target(arr, target):
    d = {}
    for i in arr:
        if i not in d.keys():
            # i is not in the list of keys, so add target / i as the value  
            div = float(target) / i
            if round(div) == div:
                # If this is a proper factor, add to the dict.
                d[i] = int(div)
    for i in arr:
        if i in d.keys() and d[i] in d.keys():
            return i, d[i]

arr1 = [3,4,-2,5,6]
arr2 = [2,4,1,6,5,40,-1]
target = 20
a,b = find_product_target(arr1, target)
print a,b
a,b = find_product_target(arr2, target)
print a,b

