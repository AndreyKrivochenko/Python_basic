from itertools import count, cycle


def print_gen_int(num):
    for val in count(start=num):
        if val == 11:
            break
        print(val)


def print_list_cycle(cnt, list_num):
    i = 1
    new_list = []
    for item in cycle(list_num):
        new_list.append(item)
        if i == cnt:
            break
        i += 1
    print(new_list)


print_gen_int(4)

list_1 = ['a', 'b', 'c']
print_list_cycle(18, list_1)
