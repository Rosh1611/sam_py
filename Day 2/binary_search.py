def binary_search(array,search_element):
    beginning=0
    end=len(array)-1
    while(beginning<=end):
        middle=(beginning+end)//2
        if(search_element==array[middle]):
            return middle
        elif(search_element>array[middle]):
            beginning=middle+1
        else:
            end=middle-1
    return -1