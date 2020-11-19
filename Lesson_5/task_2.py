with open('task_2.txt', 'r') as f_in:
    counter = [len(line.split()) for line in f_in]

for i, val in enumerate(counter):
    print(f'{i+1} string - {val} words')
print(f'All string - {len(counter)}')
