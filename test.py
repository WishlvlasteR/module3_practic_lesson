a=['Rus','Hi','Mos','cow','Tree','seVen','Do','You','Last']


def is_contains(string, list_to_search):
    string_lower = string.lower()

    # Перебор элементов списка и сравнение с искомой строкой
    for item in list_to_search:
        if string_lower == item.lower():
            return True
    return False
print(is_contains('rus',a))