def selection_sort(l):
    count = 0
    swap_happened = True
    spot_marker = 0
    while swap_happened:
        swap_happened = False
        for num in range(spot_marker+1,len(l)):
            # print('Selection sort status: ' + str(l))
            count +=1
            if l[spot_marker] > l[num]:
                l[spot_marker], l[num] = l[num], l[spot_marker]
                swap_happened = True
        spot_marker +=1
    return l

