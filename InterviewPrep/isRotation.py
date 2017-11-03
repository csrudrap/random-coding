# Implement your function below.
# Not a very good implementation, but correct.

def is_rotation(l1, l2):
    # Ex: [1,2,3,4,5] and [3,4,5,1,2]: True
    #     [1,3,4,9] and [4,9,1,8]: False
    if len(l1) != len(l2):
        return False
    # Equal length. 
    if len(l1) == 0 or len(l1) == 1:
        return True
    # Choose the first elem in list1, go through list2 to find the first occurrence and save the index in a var.
    # Check from that index onwards by (incrementing mod n) if elements are the same. If not, increment stored index till n, keep trying.
    elem = l1[0]
    index_l1 = 0
    l2_indices = []
    for i in range(len(l2)):
        if l2[i] == elem:
            l2_indices.append(i)
    count = 0
    for index_l2 in l2_indices:
        count = 0
        diff = index_l2 - index_l1
        for i in range(len(l1)):
            if l1[i] != l2[(i + diff) % len(l1)]:
                break
            count += 1
        if count == len(l1):
            return True
            
    return False

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
print is_rotation(list1, list2a) #should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
print is_rotation(list1, list2b) #should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
print is_rotation(list1, list2c) #should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
print is_rotation(list1, list2d) #should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
print is_rotation(list1, list2e) #should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
print is_rotation(list1, list2f) #should return True.

