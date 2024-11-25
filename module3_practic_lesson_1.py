    # Глобальная переменная для подсчёта вызовов
calls = 0

    # Функция для подсчёта вызовов
def count_calls():
    global calls  # Указываем, что используем глобальную переменную
    calls += 1  # Увеличиваем счётчик на 1 с каждым вызовом ф-ии


    # Функция для работы со строкой
def string_info(string):
    count_calls()  # вызываем в ф-ии ф-ию count_calls
    length = len(string)  # Подсчитываем длину строки
    upper_case = string.upper()  # Переводим в верхний регистр
    lower_case = string.lower()  # Переводим в нижний регистр
    return length, upper_case, lower_case  # Возвращаем длину и строку в верхнем, нижнем регистрах


    # Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Вызываем в ф-ии ф-ию count_calls
    string_lower = string.lower()  # Приводим строку к нижнему регистру
    # Перебор элементов списка и сравнение с искомой строкой
    for i in list_to_search:  # Перебираем список
        if string_lower == i.lower():  # Приводим список к нижнему регистру
            return True
    return False


    # Вызовы функций с произвольными данными
print(string_info("HelloWorld"))  # Пример вызова первой функции
print(string_info("Python"))  # Ещё один вызов первой функции

    # Без заданного списка ниже, cities, можно указать любой список во 2 значении функции is_contains
cities = ["New York", "Los Angeles", "ChiCago", "Houston"]
print(is_contains("chicago", cities))  # Пример вызова второй функции
print(is_contains("Miami", cities))  # Ещё один вызов второй функции

    # Вывод общего количества вызовов функций, вызовом переменной в которую сохранялось значение
print("Количество вызовов функций:", calls)
