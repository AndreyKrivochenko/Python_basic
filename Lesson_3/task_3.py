def my_func(arg_1, arg_2, arg_3):
    """
    Можно сделать так, но наверное это читерство? Недаром про позиционную передачу говорится
    arg_list = [arg_1, arg_2, arg_3]
    arg_list.sort()
    return arg_list[1]+arg_list[2]
    """
    if arg_1 <= arg_2 and arg_1 <= arg_3:
        return  arg_2 + arg_3
    elif arg_2 <= arg_1 and arg_2 <= arg_3:
        return  arg_1 + arg_3
    else:
        return  arg_1 + arg_2



print(my_func(5, 4, 0))
