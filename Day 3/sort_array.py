from quick_sort import quick_sort

def print_array(array):
    for element in array:
        print(element,end=" ")
no_of_elements=int(input("Enter The Number Of Elements : "))
array = list(map(int, input("Enter Array Elements Separated By Space: ").split()))
quick_sort(array,0,no_of_elements-1)
print_array(array)
