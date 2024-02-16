def white_walkers(line, i, previous, previous_ind, current, current_ind) -> bool:
    # условие окончания рекурсии
    if i == len(line):
        return True

    # находим очередной элемент
    if line[i] in ['0','1','2','3','4','5','6','7','8','9']:
        current: str = line[i]
        current_ind: int = i

    # если сумма предыдущего и текущего не равна 10, то текущему значению присваиваем предыдущее и
    # переходим к следующему элементу списка
    if int(current) + int(previous) != 10 and line[i] in [
        '0','1','2','3','4','5','6','7','8','9']:
        previous: str = current
        previous_ind: int = current_ind

    # проверяем количество '=' в срезе строки между двумя числами суммаа которых равна 10
    summ: int = 0
    slice_line = line[previous_ind:current_ind]
    for j in range(len(slice_line)):
        if slice_line[j] == '=':
            summ += 1

    # если количество '=' меньше 3, слодовательно, результат False
    if summ != 3 and len(slice_line) > 0 and line[i] in [
        '0','1','2','3','4','5','6','7','8','9']:
        return False

    # если перешли к следующей цифре, то текущую присваиваем переменной для предыдущего значения
    if int(current) + int(previous) == 10 and line[i] in [
        '0','1','2','3','4','5','6','7','8','9'] :
        previous = current
        previous_ind = current_ind

    i += 1

    return white_walkers(line, i, previous, previous_ind, current, current_ind)


def accept(line_original : str) -> bool:
    # обработка исключения: если цифр меньше одной
    summ_el: int = 0
    for el in line_original:
        if el in ['0','1','2','3','4','5','6','7','8','9']:
            summ_el += 1
    if summ_el < 2:
        return False

    i = 0 # счетчик
    current = 0 # текущее значение
    previous = 0 # предыдущее значение
    current_ind = 0 # индекс текущего значения
    previous_ind = 0 # индекс предыдущего значения
    return white_walkers(line_original, i, previous, previous_ind, current, current_ind)
