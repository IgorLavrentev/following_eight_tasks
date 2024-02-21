def  EEC_help(arr1: list, arr2: list) -> bool:
    # обработка исключений
    if len(arr1) != len(arr2):
        return False

    # создание двух словарей
    dictionary_1 = {}
    dictionary_2 = {}

    for i in range(len(arr1)):
        if arr1[i] in dictionary_1:
            meaning_1 = int(dictionary_1.get(arr1[i]))
            dictionary_1[arr1[i]] = meaning_1 + 1

        if arr2[i] in dictionary_2:
            meaning_2 = int(dictionary_2.get(arr2[i]))
            dictionary_2[arr2[i]] = meaning_2 + 1

        if arr1[i] not in dictionary_1:
            dictionary_1[arr1[i]] = 1

        if arr2[i] not in dictionary_2:
            dictionary_2[arr2[i]] = 1

    if dictionary_1 == dictionary_2:
        return True

    return False
