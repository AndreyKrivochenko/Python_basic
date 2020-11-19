# user_number = input('Введите число: ')
user_number = '8'
user_number = int(user_number)

my_list = [7, 5, 3, 3, 2]

if user_number > max(my_list):
    my_list.insert(0, user_number)
else:
    for i in reversed(range(len(my_list))):
        if user_number <= my_list[i]:
            my_list.insert(i+1, user_number)
            break

print(my_list)
