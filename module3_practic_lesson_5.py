    # Определение функции
def get_multiplied_digits(number):
    str_number=str(number)                                              # Преобразуем число в строку
    if len(str_number) > 1:                                             # Если длина строки больше 1, выполняем рекурсию
        first=int(str_number[0])                                        # Первая цифра
        return first * get_multiplied_digits(int(str_number[1:]))       # Возвращаем Рекурсивный вызов для оставшейся
    else:                                                               #                                   части числа
        return int(str_number[0])                                       # Иначе если длина строки 1,возвращаем саму цифру

    # Определение глобальных переменных с передачей данных аргументов в number
result_1=get_multiplied_digits(44444)
result_2=get_multiplied_digits(5555)
    # Вывод результата
print(result_1)
print(result_2)