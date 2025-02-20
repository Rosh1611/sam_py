def partition(array, low, high):
    j = low
    pivot = array[high]
    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
    array[j], array[high] = array[high], array[j] 
    return j

"""
arr=10 80 30 90 40 low=0 high=4
pivot=40
i=-1
for(j=0;j<4;j++)
{
i=-1 j=0 10<40 True
i=0 
arr= 10 80 30 90 40
i=0 j=1 80<40 False
i=0
arr= 10 80 30 90 40
i=0 j=2 30<40 True
i=1
arr=10 30 80 90 40
}
i=1 j=4 
arr=10 30 40 80 90
return 2

"""