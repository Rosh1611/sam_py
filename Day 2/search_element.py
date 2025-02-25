from binary_search import binary_search
array = list(map(int, input("Enter Array Elements Separated By Space: ").split()))
searching_element=int(input("Enter The Element You Wish To Search : "))
element_index=binary_search(array,searching_element)
print(f"{searching_element} Found At Position {element_index+1}" if element_index!=-1 else f"{searching_element} Not Present In Array")