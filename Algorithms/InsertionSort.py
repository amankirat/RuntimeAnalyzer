def insertion_sort(l):
    for num in range(1,len(l)):
        items_to_sort = l[num]
        while num >0 and l[num-1] > items_to_sort:
            l[num], l[num-1] = l[num-1], l[num]
            num = num -1
    return l


