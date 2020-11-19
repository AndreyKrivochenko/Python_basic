def show_person(**kwargs):
    person = []
    for key, val in kwargs.items():
        person.append(f'{key} - {val}')
    result = ', '.join(person)
    return result


print(show_person(first_name='Андрей', second_name='Кривоченко',
                  birth_year=1979, city='Барнаул', email='email@mail.ru', tel='+79130025458'))
