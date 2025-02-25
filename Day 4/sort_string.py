def insertion_sort(string):
    arr=list(string)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key.lower() < arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return ''.join(arr)
input_string=input("Enter A String : ")
print(f"The Sorted String : {insertion_sort(input_string)}")