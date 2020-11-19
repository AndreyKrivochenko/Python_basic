with open('task_5.txt', 'w') as file:
    file.write('23 2 33 43 2 555 65 44 30 87 6 99 11')

with open('task_5.txt', 'r') as file:
    numbers = file.read().split()

print(sum([int(num) for num in numbers]))
