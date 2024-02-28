# функция сортировки списка
def sorting_list(trc_1, Lo, Mid, Hi) -> list:
    if Mid > Hi: # условие окончания рекурсии
        return trc_1

    if trc_1[Mid] == 2:
        trc_1[Mid], trc_1[Hi] = trc_1[Hi], trc_1[Mid]
        Hi -= 1

    if trc_1[Mid] == 1:
        Mid += 1

    if trc_1[Mid] == 0:
        trc_1[Mid], trc_1[Lo + 1] = trc_1[Lo + 1], trc_1[Mid]
        Lo += 1
        Mid += 1

    return sorting_list(trc_1, Lo, Mid, Hi)

# функция для получения исходных данных (строки)
def TRC_sort(trc: list) -> list:
    # работа с исключениями
    if trc == [0,1] or trc == [1]:
        return trc
    l_initial  = -1
    m_initial  = 0
    h_initial  = len(trc) - 1

    return sorting_list(trc, l_initial, m_initial, h_initial)
