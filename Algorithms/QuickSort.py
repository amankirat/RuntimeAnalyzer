def quick_sort(l):
    if len(l) <2:
        return l
    else:
        pivot = l[-1]
        smaller, equal, larger = [],[],[]
        for num in l:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quick_sort(smaller) +equal + quick_sort(larger)
