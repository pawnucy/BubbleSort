def bubble_sort(lst):
    # Function compares two elements and swap when they not in order.
    n = len(lst)
    for a in range(n):
        for b in range(0, n - a - 1):
            if lst[b] > lst[b+1]:
                lst[b], lst[b+1] = lst[b+1], lst[b]
    return (lst)

def sorted_list():
    # Function to test bubble sort with various input lists.
    numbers = [[], [1,2,5,3,1,7,9,1,12,83,1,5,3,2], [1,1,1,1,1,1,1,2,1,1,1], [2,2,2,2], [1,2], [2,1]]
    for number in numbers:
        sorted_numbers = bubble_sort(number)
        print(sorted_numbers)

sorted_list()


