# user_number = input('Введите число: ')
user_number = '4'
user_number = int(user_number)

my_list = [7, 5, 3, 3, 2]
my_list.reverse()

if user_number > max(my_list):
    my_list.append(user_number)
else:
    for i in range(len(my_list)):
        if user_number <= my_list[i]:
            my_list.insert(i, user_number)
            break

my_list.reverse()
print(my_list)
