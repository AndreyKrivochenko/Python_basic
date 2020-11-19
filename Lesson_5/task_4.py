translate = {
    'One': 'один',
    'Two': 'два',
    'Three': 'три',
    'Four': 'четыре'
}
with open('task_4_out.txt', 'w') as out_file:
    with open('task_4.txt', 'r') as in_file:
        for line in in_file:
            for key in translate:
                if line.find(key) != -1:
                    out_file.write(line.replace(key, translate[key]))
