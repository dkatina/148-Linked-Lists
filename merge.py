

l1 = [1,3,5,7,9]
l2 = [2,4,16,18]

def merged(list1, list2):

    one = 0
    two = 0
    merged = []

    while one < len(list1) and two < len(list2):

        if list1[one] < list2[two]:
            merged.append(list1[one])
            one += 1

        else:
            merged.append(list2[two])
            two += 1

        
    if one == len(list1):
        merged = merged + list2[two:]
    else:
        merged = merged + list1[one:]

    return merged

print(merged(l1,l2))
