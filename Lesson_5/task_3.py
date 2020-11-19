# Печатаем на экран список сотрудников с зарплатой меньше 20000
def print_sal_min(workers: dict):
    print(f'Работники с зарплатой меньше 20000:')
    for name in workers:
        if workers[name] < 20000:
            print(f'{name} - {workers[name]}')


# Считаем среднюю зарплату
def calc_aver_sal(workers: dict):
    return int(sum(workers.values()) / len(workers))


with open('task_3.txt', 'r') as f_in:
    user_list = f_in.read().splitlines()

salary_list = [string.split() for string in user_list]

salary = {}
for item in salary_list:
    salary[item[0]] = int(item[1])

print_sal_min(salary)
print(f'\nСредняя зарплата - {calc_aver_sal(salary)}')
