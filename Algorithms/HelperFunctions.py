import time
from random import randint
from Algorithms.BubbleSort import bubble_sort
from Algorithms.InsertionSort import insertion_sort
from Algorithms.MergeSort import divide_arr
from Algorithms.SelectionSort import selection_sort
from Algorithms.QuickSort import quick_sort

def generate_random(end,limit):
    newlist = [randint(1,end) for x in range(limit)]
    return newlist

def analyze_func(func_name, arr):
    tic = time.time()
    print(func_name(arr))
    toc = time.time()
    sec = toc - tic
    print(f"{func_name.__name__.capitalize()} = Elapsed time: {sec:.5f}")

def select_sort_algo(selected_option, l):
    if selected_option == 1:
        analyze_func(bubble_sort, l.copy())
    elif selected_option == 2:
        analyze_func(bubble_sort, l.copy())
    elif selected_option == 3:
        analyze_func(quick_sort, l.copy())
    elif selected_option == 4:
        analyze_func(insertion_sort, l.copy())
    elif selected_option == 5:
        analyze_func(divide_arr, l.copy())
    elif selected_option == 6:
        analyze_func(selection_sort, l.copy())