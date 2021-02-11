def merge_sorted(l1,l2):
    i,j =0,0
    sorted_arr = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            sorted_arr.append(l1[i])
            i +=1
        else:
            sorted_arr.append(l2[j])
            j+=1
    while i < len(l1):
        sorted_arr.append(l1[i])
        i += 1
    while j < len(l2):
        sorted_arr.append(l2[j])
        j += 1
    return sorted_arr

def divide_arr(l):
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l)//2
        l1 = divide_arr(l[:middle])
        l2 = divide_arr(l[middle:])
        return merge_sorted(l1, l2)

