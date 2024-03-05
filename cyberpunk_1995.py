def army_communication_matrix(n: int, matrix) -> str:
    m = n - 1 # размер подматрицы
    result_sum = 0 # сумма числе подматрицы
    result = '' # строка для представления результата
    while m >= 2:
        for x in range(len(matrix[0]) - m + 1):
            for y in range(len(matrix) - m + 1):
                s_111 = []
                summ = 0
                for k in range(m):
                    s_1 = matrix[y + k]
                    s_11 = s_1[x : x + m]
                    s_111.append(s_11)
                    # вычисляем сумму подматрицы
                    summ_0 = sum(s_111[k])
                    summ += summ_0
                # проверка очередного значения суммы чисел подматрицы с текущим максимальным
                if summ > result_sum:
                    result_sum = summ
                    result = str(x) + ' ' + str(y) + ' ' + str(m)
        m -= 1

    return result
