def massdriver(activate: list) -> int:
    dictionary = {}
    # добавление всех значений и их количества повторений в словарь
    for i in range(len(activate)):

        if activate[i] in dictionary: # если значение есть в словаре
            meaning_1 = int(dictionary.get(activate[i]))
            dictionary[activate[i]] = meaning_1 + 1

        if activate[i] not in dictionary: # если значения нет в словаре
            dictionary[activate[i]] = 1

    for key, value in dictionary.items(): # выбираем первое повторяющееся значение
        if value > 1:
            return activate.index(key)

    return -1
