list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_2 = [num for num in list_1[1:] if num > list_1[list_1.index(num)-1]]

print(list_2)
