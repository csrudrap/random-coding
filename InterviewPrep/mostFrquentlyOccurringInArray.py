def most_frequent(arr):
    # For [1,3,1,3,2,1], we should get 1
    # For [1,3,1,3,2,2,2,1,4,3,1,2,3,4,2,1,2,2], we should get 2
    d = {}
    for i in arr:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    max_val = 0
    max_key = 0
    for i in d.keys():
        if d[i] > max_val:
            max_val = d[i]
            max_key = i 
    return max_key

arr1 = [1,3,1,3,2,1]
print most_frequent(arr1)
arr2 = [1,3,1,3,2,2,2,1,4,3,1,2,3,4,2,1,2,2]
print most_frequent(arr2)
