
user = {'login': "login_1", 'password': 'password_1'}
users = {
    '10a': {
        'Arseniy': 16,
        'Vanya': 16,
        'Kostik': 16,
    },


    '10b': {
        "Arseniy": 16,
        "Andrey": 15,
        "Egor": 14,
    }
}



def recursive_search(value, search_by):
    pass


def recursive(dictionary, search_by):
    """Рекурсивный поиск по вложеным словарям

    :param dictionary: передоваемый словарь(словарь по которому будем производить поиск)
    :param search_by: параметр по которому будем производить поиск
    :return: результат поиска
    """
    if search_by in dictionary.keys():
        return dictionary[search_by]

    for value in dictionary.values():
        if type(value) is dict:
            search_by = recursive_search(value, search_by)

    if search_by is not None:
        return search_by
    else:
        return "gg"

search = input('name')
print(f'{search}: {recursive_search(users, search)}')


print()