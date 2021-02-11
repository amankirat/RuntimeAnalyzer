def bubble_sort(l):
    count = 0
    for num1 in range(len(l) - 1):
        # print('Bubble sort status: '+  str(l))
        for num in range(len(l)-1):
            count +=1
            if l[num] > l[num+1]:
                l[num], l[num + 1] = l[num+1], l[num]
    return l