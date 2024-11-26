
                                            #Module 3

                                    #Lesson 1 : ПРОСТРАНСТВО ИМЁН


# Существует несколько видов пространства имен :


    # 1. Встроенное пространсво имён - это имена которые встроены уже в значение этой функции

    # 2. Глобальное пространсво имён - имена которые есть в программе , но не включая локальное пространство.
         # к ним можно обращаться в любом месте программы и будет виден результат их имён/значений
         #Пример:
                # a=5
                # b=22

    # 3. Локальное пространсво имён - это имена которые используются в самой функции( в теле функции) и код программы
         # видит эти переменные только внутри самой ф-ии и существуют они только внутри этой ф-ии,
         # если их вызвать отдельно от ф-ии, будет ошибка, но из локального пространства ф-ии иожно обращаться к глобал.
         # пространству, так же можно применять названия переменных такие же как и в глобальном пространстве, тогда
         # локально вызываться будут переменные которые локально в функции т.к. вызов тоже идёт локально, но если
         # вызывать переменные не в теле ф-ии будут вызваны глобальные и они как были так и останутся с прежними значениями

         # Для того чтобы из локального пространства как то влиять на глобальное пространство в локальном пространстве
         # используется команда global перед использованием переменных
         #Пример:
                # def printer():
                    # c=15
                    # d=20
                    # print(c,d ' local ')   - обращение по локальному пространству непосредственно внутри ф-ии
                    # print(a,b ' global ')  - из локал.пространства ф-ии обращаемся к глобал пространству
                #printer()

                # def printer():
                    # global                 - команда которая преобразовала глобальные переменные a,b из локал,прост,
                    # a=10
                    # b=10
                    # c=15
                    # d=20
                    # print(c,d ' local ')   -
                    # print(a,b ' global ')  -
                #printer()


                                            # MODULE 3 ПОДРОБНЕЕ О ФУНКЦИЯХ
                                            # LESSON 2
                                            # СПОСОБЫ ВЫЗОВА ФУНКЦИИ


    # 1. Если в принимающей ф-ии есть 3 параметра, то именно 3 аргумента мы и должны указать при вызове ф-ии

        # Если аргументы указаны, то при вызове ф-ии можно не указывать их, при указании все же их при вызове
        #они меняются, также можно их переназначить точечно:
        #Примет:
            # def print_params(a=1,b=2,c=3)
            # print_params(2,5,c='String')

    # 2. Перед именованым всегда должны идти позиционные, но если они именнованы, то можно их передавать не по порядку
        # Приммер: print_params(c = 'strings, a = 2, b = True)

    # 3. * - заставляет параметры после неё писать именованными, если написать позиционные после * будет ошибка
        # Пример def print_params(a=1,*,b,c)
        # print_params(2,5,c='String') - ошибка т.к. b,c должны указаться как именованные через =   b=4-именовали



                                            # MODULE 3 ПОДРОБНЕЕ О ФУНКЦИЯХ
                                            # LESSON 3
                                            # ПАРАМЕТРЫ ПО УМОЛЧАНИЮ В НУТРИ ФУНКЦИИ


    # 1. Значения по умолчанию (с заданными значениями) всегда идут после значений без заданных значений
# функция имеет возможность принимать параметры по умолчанию, что позволяет нам в момент вызова не передавать никаких
# аргументов. Но, если мы работаем с параметрами по умолчанию, мы их задаём либо конечным элементам, либо уж всем,
# которые присутствуют у нас в функции. И в качестве этих самых значений по умолчанию мы используем неизменяемые объекты.
# Когда мы работаем с параметрами по умолчанию, в качестве этих параметров мы указываем неизменяемые объекты.
# Нужно помнить, что эти значения параметров создаются не в момент, когда мы вызываем функцию, а создаются при её
# определении.

    # 2. Важно! Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
         # В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
         # def a(my_list = [])) – это приводит к ошибкам!

         # Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
         # def append_to_list(item, list_my=None):
         #   if list_my is None:
         #    list_my = []
         #   list_my.append(item)
         # print(list_my)

                                            # MODULE 3 ПОДРОБНЕЕ О ФУНКЦИЯХ
                                            # LESSON 4
                                            # РАСПАКОВКА ПОЗИЦИОННЫХ ПАРАМЕТРОВ


    #1. * Используется для упаковки/распаковки позиционных параметров в которых содержится один элемент(списки,кортеж,
        # множества и тд), при упаковке изначально они все упаковываются в кортеж
        #
        # Пример: упаковки: def print_params(*args):
                                #print(params)
                                #print_params(*params 1,2,3,4,5,6,7,8)

        # Пример распаковки: def print_params(a,b,c):
                                #print(a,b,c)
                             #list_=[1,2,3]
            #Для того чтобы значения списка встали на место параметров надо:
                             # print_params(*list_) - перед передачей листа в () ставится *
        # Важно обращать внимание на кол-во значений в списке и в функции
        # print_params(1, *list_)  - еденичка встанет на параметр "а", а лист распакуется в параметры b, c
        # или наоборот аргумент передать в значение "с" после распаковки list_

    #2. ** Используется для упаковки/распаковки именованных параметров - это словари
        # Имена ключей должны соответствовать именам параметрам
        #Пример: def print_params(a,b,c):


                 #dict_={'a':1,'b':2,'c':3}         #dict_={'a':1,'b':2,'d':3}
                 #print_params(**dict_)             # Будет ошибка так как ключ d не соответствует параметру с
                                        # но можно использовать в параметрах **kwargs тогда словарь встанет без ошибок

    #3. Как правило: *kwargs используется после *args так как именованные параметры идут после позиционных

    #4. С помощью цикла for можно проходиться по параметрам
            #Пример: def print_params(**kwargs):
                        # for ley in kwargs
                            #print(key)


                                            # MODULE 3 ПОДРОБНЕЕ О ФУНКЦИЯХ
                                            # LESSON 5
                                            # ПРОИЗВОЛЬНОЕ ЧИСЛО ПАРАМЕТРОВ

 # В случаях когда нам не известно сколько параметров нам потребуется, то в назанчении функции указываем *перед именем
 # Пример 1:
        # def test_func(*params):    # если вызвать эту функцию без передачи аргументов увидем: пустой кортеж
        # print (*params)            # и если мы передаем параметры ф-ии через:
                                     # test_func(1,2,3,4,5) то все эти параметры записываются в кортеж
 #Пример 2:
        # def summator(txt,*values):                # ф-ия принимает 2 значения в txt - одно и в *values записывает
        #   s=0                                     # в виде кортежа все остальные значения которые будут введены через,
        #   for i in values:                        # s изначальный счетчик в который будут записываться значения
        #       s+= i                               # так как у нас цикл for то он перебирает значения находящиеся в
        #   return f'{txt} {s}'                     # в объекте и прибавляет последующее к значению которое было в s
        #print(summator('Сумма числел: ', 2,3,4))   # записанно: итого из этого примера он складывает все значения
                                                    # которые ввёл пользователь
 # Пример 3:
        # def info(**valuse):                       # данная ф-ия объявляет о том что мы не знаем сколько в ней будет
        # print(values)                             # именованных параметров
        # for key,value in values.items()           # c помощью цикла for можно пройтись по словарю и сделать более
        # print(key,value)                          # удобночитаемый вывод.
        # info(name='Den', courses='python')        # Присвоение в передачи(вызове) ф-ии словарю происходит через =

 # Пример 4:
        # def ...(value,*types,name='Rus',**values) # Где value - Обычный позиционный параметр
                                                    # *types - Произвольное кол-во позиционных параметров
                                                    # name= - Именованный параметр
                                                    #**values - Произвольное кол-во именованных параметров
        # Соблюдение объявления параметров именно так иначе ф-ия не будет объявлена будет ошибка
        # назначение идёт от меньшей важности к большей, а вывод наоборот: выводится от высшей важности к низшей

 # итого следует что в функции можно использовать все виды параметров при объявлении ф-ии как: позиционные так и
 # именованные, параметры с переменным количеством, с параметрами по умолчанию, в том числе есть возможность
 # использовать произвольное количество именованных параметров.

 # Пример 5:
        # def my_sum(n,*args,txt='Сумма чисел') # Ф-ия принимает 3 параметра :позиционный,произвол.позиц.и именованный
        #   s=0                                 # переменная с 0 для перебора в цикле for
        #   for i in range(len(args)):          # перебираем кол-во значений по индексу
        #       s+= args[i] **n                 # берём элемент по индексу возводим в степень и прибавляем к s
        #   print(txt + ':', s)
        # my_sum(1, 1, 2, 3, 4, 5)
        # my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")


                                            # MODULE 3 ПОДРОБНЕЕ О ФУНКЦИЯХ
                                            # LESSON 6
                                            # РЕКУРСИЯ

    # Рекурсия - это способ описания ф-ии когда ф-ия вызывает саму себя(как работает функция).
    # во избежании ошибок у рекурсии обязательно должен быть выход
    # Когда есть возможность избежать рекурсиюю лучше, её избегать, впринцепи любую рекурсию можно заменить циклом,
    # как и любой цикл можно заменить рекурсией
        # Пример:
        # def summa(n):
        #   if n == 0
        #       return 0
        #   else:
        #       return n + summa(n -1)
        # print(summa(5))
    # Стэк - это способ организации данных в памяти ПК, по принцепу, последний пришел - первым вышел.
    # 'LIFO'(last in first out)-это значит что последний элемент, который был добавлен в стек будет взят из него первым,
    # добавлять новые элементы и удалять из него существующие мы можем только с одного конца который называется вершиной.
    # Чаще всего стеки организуют из динамических массивов и связанных списков
    # Динамический массив-это такой массив в котором может увеличиваться или уменьшаться размер в процессе выполнения программы

        # Пример стека:                            #Добавляем элементы и убираем в порядке LIFO
        # def recursion():                         # работает как детская игрушка пирамидка
        # recursion()                              # первый элемент который был в списке - был убран последним.
        #
        #recursion()                               # Каждый раз когда мы вызываем ф-ию, мы забиваем стэк вызовов
        # stack = []                               # Стек вызовов это структура данных которая управляет
        # stack.append(1)                          # вызовами ф-ии в момент выполнения программы
        # print('Добавили элемент' , stack)        # область памяти, где хранятся точки перехода, называется
        # stack.append(2)                          # стеком вызова и в этой точке хранится все чтоб ПК смог
        # print('Добавили элемент' , stack)        # вернуться быстро к выполнению какого-то основного кода
        # stack.append(3)                          # Тоесть это то место куда ПК должен перейти к началу выполнения
        # print('Добавили элемент' , stack)        # какой-то подпрограммы, и если в каком то месте произойдет
        # print(stack)                             # вызов ф-ии внутри другой ф-ии то ПК ставит на паузу первую ф-ию
        # stack.pop()                              # сохраняя в стеке точку вызова и переходит к выполнению другой ф-ии
        # print('Убрали элемент', stack)           # такой принцип работает для любой степени вложенности
        # stack.pop()
        # print('Убрали элемент', stack)
        # stack.pop()
        # print('Убрали элемент', stack)

    # Если где-то появляется ошибка RecursionError: maximum recursion depth exceeded- значит где-то не вышли из рекурсии


























