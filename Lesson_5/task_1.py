user_input = ['string_1', 'string_2', 'string_3']

with open('task_1.txt', 'w') as f_out:
    for string in user_input:
        f_out.write(f'{string}\n')