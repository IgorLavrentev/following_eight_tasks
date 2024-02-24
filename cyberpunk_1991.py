def artificial_muscle_fibers(arr: list) -> int:
    flag = False
    quantity = 0
    # сортировка списка по убыванию
    for i in range(len(arr)): # i проходит от 0 до длины списка
        counter = i + 1  # при каждом проходе задается новое значение counter
        for j in range(counter, len(arr)): # counter проходит от i + 1 до длины списка
            # сравнение i-го элемента с индексом элемента 'counter'
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        counter += 1

    # проверка двух ближайших значений
    # если значения совпадают впервые, то +1 к ответу
    for k in range(len(arr) - 1):
        if arr[k] == arr[k + 1] and flag is False:
            quantity += 1
            flag = True
        if arr[k] != arr[k + 1]:
            flag = False

    return quantity
