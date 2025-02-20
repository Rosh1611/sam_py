number_of_oranges=int(input())
oranges = list(map(int, input().split()))
chosen_orange_diameter=oranges[-1]
for diameter in oranges[::-1]:
    if diameter>chosen_orange_diameter:
        oranges.append(diameter)
        oranges.remove(diameter)
    #print(oranges,diameter)
print("Final :",oranges)