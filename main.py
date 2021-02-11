from Algorithms.HelperFunctions import generate_random, select_sort_algo

selected_option = int(input("""Select following sorting techniques from the list below:
1. Bubble sort
2. Quick sort
3. Insertion sort
4. Merge sort
5. Selection sort:
"""))
size = int(input("Enter the size of the list:"))
max = int(input("Enter the max range of integers:"))
l = generate_random(size, max)
select_sort_algo(selected_option,l)




