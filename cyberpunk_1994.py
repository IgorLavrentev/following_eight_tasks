def matrix(n: int, m: int, matrix: list) -> list:
    final_list = []
    counter = 0
    if m % 2 == 0:
        limitation = m / 2
    if m % 2 != 0:
        limitation = (m // 2) + 1

    while counter < limitation:
        # 1 из 4 верхняя строка матрицы
        upper_part = matrix[0 + counter]
        for i in range(0 + counter, n - counter):
            final_list.append(upper_part[i])

        if len(final_list) == len(matrix) * n:
            return final_list

        # 2 из 4 строка матрицы правая часть
        for j in range(1 + counter, m - 1 - counter):
            right_part = matrix[j]
            final_list.append(right_part[len(right_part) - 1 - counter])

        # 3 из 4 нижняя строка матрицы
        lower_part = matrix[m - 1 - counter]
        lower_part = lower_part[::-1]
        for k in range(0 + counter, n - counter):
            final_list.append(lower_part[k])

        if len(final_list) == len(matrix) * n:
            return final_list

        # 4 из 4 строка матрицы левая часть
        for h in range(m - 2 - counter, 0 + counter, -1):
            left_part = matrix[h]
            final_list.append(left_part[0 + counter])

        counter += 1

    return final_list
