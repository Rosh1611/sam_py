def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = key
        print(f"Iter {i}: {arr}")
l1=[4,1,2,0]
insertion_sort(l1)
print(l1)

"""
4 3 2 10 12 1 5 6
3 4 2 10 12 1 5 6
2 3 4 10 12 1 5 6
2 3 4 10 1 12 5 6
2 3 4 1 10 12 5 6
2 3 1 4 10 12 5 6
2 1 3 4 10 12 5 6
1 2 3 4 10 12 5 6

"""