def arrange():
    no_of_boys=no_of_girls=int(input())
    boys_height = sorted(list(map(int, input().split())))
    girls_height = sorted(list(map(int, input().split())))
    students_height = sorted(boys_height+girls_height)
    if students_height[::2]==boys_height:
        return("YES" if(students_height[1::2]==girls_height) else "NO")
    elif students_height[1::2]==boys_height:
        return("YES" if(students_height[::2]==girls_height) else "NO")
    else:
        return("NO")
no_of_test_cases=int(input())
output_list=[]
for i in range(no_of_test_cases):
    output_list.append(arrange())
for output in output_list:
    print(output)