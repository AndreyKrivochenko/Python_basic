def int_func(text):
    result = f'{chr(ord(text[0])-32)}{text[1:]}'
    return result


def cap_string(text):
    text_list = text.split()
    for i in range(len(text_list)):
        text_list[i] = int_func(text_list[i])
    result = ' '.join(text_list)
    return result


print(int_func('text'))
print((cap_string('text my new function')))