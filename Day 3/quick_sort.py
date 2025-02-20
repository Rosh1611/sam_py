from array_partition import partition

def quick_sort(array, beginning, end):
    if beginning < end:
        pivot_index = partition(array, beginning, end)
        quick_sort(array, beginning, pivot_index-1)
        quick_sort(array, pivot_index+1, end)