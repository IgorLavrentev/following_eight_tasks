def digital_rain(col):

    # считаем количество нулей и единиц
    one = col.count('1')
    zero = col.count('0')

    # выбираем наименьшее
    if one > zero:
        minn = zero
    if one <= zero:
        minn = one

    # работа с исключениями: если меньшее равно 0
    if minn == 0:
        return ''

    j_end = minn # количество итераций будет ограничино значением наименьшего
    for _ in range(j_end):
        for i in range(len(col), minn*2 - 1, -1): # начинаем с конца строки
            # выделяем чать строки равную наименьшему умноженному на 2
            part_of_line = col[i - minn*2 : i]
            one = part_of_line.count('1')
            zero = part_of_line.count('0')
            # если в выделенной части строки количество нулей и единиц совпали это и есть результат
            if one == zero:
                return part_of_line
        minn -= 1
        if minn == 0:
            return ''
    return ''
