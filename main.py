# Python: основы и применение
# https://stepik.org/course/512/syllabus



# 1.1 Введение 8 из 9 шагов пройдено

# Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.
#
# Вашей программе на вход подается последовательность строк.
# Первая строка содержит число n (1 ≤ n ≤ 100).
# В следующих n строках содержится по одному целому числу.
#
# Выведите одно число – сумму данных n чисел.

# Sample Input 1:
# 2
# 2
# 3
# Sample Output 1:
# 5
# Sample Input 2:
# 2
# -2
# -2
# Sample Output 2:
# -4

# 1.1 Введение 8 из 9 шагов пройдено. Correct answer
"""n = int(input())
sum = 0
for i in range(n):
    i = int(input())
    sum += i
print(sum)"""




######




# 1.2 Модель данных: объекты 3 из 9 шагов пройдено
# Идентификатор объекта
"""
x = [1, 2, 3]
a = 2
print(id(x))                        #140436763624320
print(id([1, 2, 3]))                #140436763624512
print(id(a))                        #4526258560
print(id(2))                        #4526258560

a = 2
print(a, id(a))                     #4461799808
b = 3
print(b, id(b))                     #4461799840
c = [a, b]
print(c, id(c))                     #140409168282688
b = 7
print(b, id(b))                     #4461799968
print(c, id(c))                     #140409168282688
print(id(2))                        #4461799808
print(id(7))                        #4461799968

print()

x = 3
y = x
print(id(3))                        #4400814496
print(id(x))                        #4400814496
print(id(y))                        #4400814496
print(y is x)

# Итог, "простые" объекты как мелкие числа или короткие строки,
# будут ссылаться на один и тот же id, так как они не изменяемые и это можно позволить.
# Большие числа, длинные строки, другие объекты будут разными, даже при одном и том же значении.

import sys
print(sys.getrefcount(2))           #115
"""


"""x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)"""

# Стоит обратить внимание что y += [4] работает как append,
# а y = y + [4] создает новый объект, при этом t += '4'
# создает новый объект в отличии от того же оператора для списка.


"""print(type(type(type(1))))              #<class 'type'>"""









######




# 1.2 Модель данных: объекты 8 из 9 шагов пройдено

# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
#
# Вашей программе доступна переменная с названием objects,
# которая ссылается на список, содержащий не более 100 объектов.
# Выведите количество различных объектов в этом списке.

# Формат ожидаемой программы:

# ans = 0
# for obj in objects: # доступная переменная objects
#     ans += 1
#
# print(ans)


# 1.2 Модель данных: объекты 8 из 9 шагов пройдено. Correct answer
"""
objects = [1, 2, 3, 4, 5, 1, 1, 1, 2, 2, 1, 1]
# objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
# objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2], [1,2], [1,2]]

lst = []
for i in objects:
    print(id(i))
    if id(i) not in lst:
        lst.append(id(i))
ans = len(lst)
print(ans)"""


# 1.2 Модель данных: объекты 8 из 9 шагов пройдено. Not my code
"""
# Классно, что это штука не впереди соседа ищет, а сзади!
n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
            break

print(ans)
"""


# 1.2 Модель данных: объекты 8 из 9 шагов пройдено. Not my code
"""
print(len(set(map(id, objects))))
"""


# 1.2 Модель данных: объекты 8 из 9 шагов пройдено. Not my code
"""p = {}
for i in objects:
    p[id(i)] = id(i)
print(len(p))"""







######




# 1.3 Функции и стек вызовов 6 из 15 шагов пройдено
"""a = []

def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)                        #'arg1', 'arg2', 'foo']"""

# Аргументы функции - a.append("arg1") и a.append("arg2").
# При запуске функции они инициализируются, т.е. дважды срабатывает функция append.
# Для которой тоже инициализируется аргумент (создаётся объект "arg1" при первом вызове функции и "arg2" при втором).
# Таким образом, сначала в список a добавляются строки "arg1" и "arg2".
#
# Затем уже срабатывает тело функции, добавляющее в список a строку "foo".







######




# 1.3 Функции и стек вызовов 6 из 15 шагов пройдено
"""def g():
    print("I am in function g")


def f():
    print("I am in function f")
    g()
    print("I am in function f")


print("I am outside of any function")
f()
print("I am outside of any function")"""

# I am outside of any function
# I am in function f
# I am in function g
# I am in function f
# I am outside of any function




# def h():
#     print("- H")
#     print("- 12")
#     print("H - end")
#
# def f():
#     print("- F")
#     g(h)
#     print("F - end")
#
# def g(a):
#     print("- G - ",a)
#     a()
#     print("G - end")
#
# print("\nMODULE")
# g(f)

"""mystack = ['module']


def h():
    mystack.append("h")
    print("The beginning of h function is: {}".format(mystack))
    print(12)
    mystack.append("print")
    print("The beginning of print function is: {}".format(mystack))
    mystack.pop()
    print("The end of print function is: {}".format(mystack))
    mystack.pop()
    print("The end of h function is: {}".format(mystack))"""


"""def f():
    mystack.append("f")
    print("The beginning of f function is: {}".format(mystack))
    g(h)
    mystack.pop()
    print("The end of f function is: {}".format(mystack))


def g(a):
    mystack.append("g")
    print("The beginning of f function is: ".format(mystack))
    a()
    mystack.pop()
    print("The end of g function is: {}".format(mystack))

g(f)"""






######






# 1.3 Функции и стек вызовов 9 из 15 шагов пройдено

# Напишите реализацию функции closest_mod_5, принимающую в качестве
# единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
#
# y больше или равно x
# y делится нацело на 5




# 1.3 Функции и стек вызовов 9 из 15 шагов пройдено. Correct answer
"""def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return (x + 5) - x % 5"""



# 1.3 Функции и стек вызовов 9 из 15 шагов пройдено. Not my code
# Пример рекурсивного решения
"""def closest_mod_5(x):
    return x if x % 5 == 0 else closest_mod_5(x + 1)"""

# 1.3 Функции и стек вызовов 9 из 15 шагов пройдено. Not my code
# Точная формула для поиска ответа: подходит для любого числа
"""def closest_mod_5(x):
    return (x + 4) // 5 * 5"""





# 1.3 Функции и стек вызовов 12 из 15 шагов пройдено
# Как располагать аргументы внутри функции

"""a = 1
b = 2
lst = [5, 6, 7, 8]
dct = {"1": 11, "2": 22}
print(a, b, lst, dct)


def pr(aa, bb, cc, *llst, **ddct):
    print(aa)  # =a
    print(bb)  # =b
    print(cc)  # возьмётся из списка
    print(llst)  # остатки списка в виде кортежа
    print(lst)  # глобальная переменная
    for k in ddct:
        print(k, ddct[k])
    print(ddct)  # словарь в к-й попали dct, r=8,t=6
    print(*llst)  # элементы кортежа
    print(*ddct)  # ключи словаря
    print(*dct)  # глобальная переменная


pr(a, b, *lst, **dct, r=8, t=6)"""



"""def function_name([ positional_args,
                                   [ positional_args_with_default,
                                   [ *pos_args_name,
                                   [ keyword_only_args,
                                   [ **kw_args_name]]]]]):
-позиционные аргументы: a, b, c
-позиц. аргументы со значением по умолчанию: d=0, e=True
-дополнительные позиционные аргументы (которые в инициализации не участвовали) 
отправляются в кортеж (*args) - в том порядке, в котором передаем их в функцию: *args или *lst
-блок аргументов, которые можно передать только по имени: f, g, h=10
-именованные аргументы которые в инициализации не участвовали отправляются в словарь: **kwarqs
Пример:
def printab(a, b=10, *args, c=10, d, **kwarqs):
    print(...)
printab(15, d=15)"""


"""
def printab(a=50, b=100, *args, **kwargs):
    print('a =', a)
    print('b =', b)
    print('additional positional arguments:')
    for i in args:  # распечатка кортеджа
        print(i)
    print('additional named arguments:')
    for key in kwargs:  # распечатка словаря
        print(key, '=', kwargs[key])

printab(10, 20, 25, 35, 45, 50, 60, c=30, d=40, jimmi=12"""









# 1.3 Функции и стек вызовов 12 из 15 шагов пройдено
# Помогает понять как работают аргументы врнутри функции.
"""def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(5,5,5,5,1))"""






'''
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
x = 4
print(x, fib(x))'''

"""def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))"""









######









# 1.3 Функции и стек вызовов 15 из 15 шагов пройдено

# Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
# Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
# Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).
#
# Пример:
# Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
# Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
# Различных сочетаний три, поэтому C(3, 2) = 3.
#
# Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно
# единственным образом, а именно, ничего не выбрать.
# Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например,
# из трех элементов выбрать пять.
#
# Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
#
# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
#
# Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).


# 1.3 Функции и стек вызовов 15 из 15 шагов пройдено. Correct answer
"""n, k = map(int, input().split())
def C(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    return C(n - 1, k) + C(n - 1, k - 1)
print(C(n, k))"""



# 1.3 Функции и стек вызовов 15 из 15 шагов пройдено. Not my code
"""def c(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)

n, k = map(int, input().split())
print(c(n, k))"""


# 1.3 Функции и стек вызовов 15 из 15 шагов пройдено. Not my code
# Пример эффективного решения:
# в данном решении мы посчитаем все значения c(n, k) лишь единожды

"""n, k = map(int, input().split())

sz = max(n, k) + 1
c = [[0] * sz for _ in range(sz)]

c[0][0] = 1
for i in range(1, sz):
    for j in range(i + 1):
        c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

print(c[n][k])"""







######





# 1.4 Пространства имён и области видимости 2 из 10 шагов пройдено
"""import builtins
print(dir(builtins))"""


# x, y = 1, 2
#
# def foo():
#     global y
#     if y == 2:
#         x = 2
#         y = 1
#
# foo()
# print(x) # 1
# if y == 1:
#     x = 3
# print(x) # 3








######






# 1.4 Пространства имён и области видимости 9 из 10 шагов пройдено

# Реализуйте программу, которая будет эмулировать работу с пространствами имен.
# Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
#
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
#
# Вашей программе на вход подаются следующие запросы:
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет
#     взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует


# Sample Input:
# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b

# Sample Output:
# global
# None
# bar
# foo

"""n = int(input())
globals = dict()
foo = dict()
bar = dict()
names = dict()

globals = ['a']
foo = []
bar = []
names = []


# for i in range(n):
#     q1, q2, q3 = input().split(' ')
#     print(q1, q2, q3, sep='\n')

q1 = 'create'
q2 = 'foo'
q3 = 'global'

if q1 == 'add':
    if q2 == 'global':
        globals.append(q3)

if q1 == 'create':
    names.append(q2)




print('global = ', globals,
      'foo =', foo,
      'bar =', bar,
      'names =', names,)
"""



"""scopes = {'global': {'parent': None, 'variables': set()}}
scopes = {'global': {'parent': None, 'variables': set()}, 'foo': {'parent': 'global', 'variables': set('a')}}

cmd = 'create'
name = 'foo'
var = 'global'

cmd = 'add'
name = 'global'
var = 'a'

cmd = 'get'
name = 'foo'
var = 'a'

def add(name, var):
    scopes[name]['variables'] = var

def create(name, var):
    scopes[name] = {'parent': var, 'variables': set()}

def get(name, var):
    if var in scopes[name]['variables']:
        print(name)
    elif scopes[name]['parent'] == None:
        print(None)
    else: get(name = scopes[name]['parent'], var = var)

if cmd == 'add':
    add(name, var)
if cmd == 'create':
    create(name, var)
if cmd == 'get':
    get(name, var)


print(scopes)"""




# 1.4 Пространства имён и области видимости 9 из 10 шагов пройдено. Correct answer

"""
def add(name, var):
    scopes[name]['variables'].add(var)

def create(name, var):
    scopes[name] = {'parent': var, 'variables': set()}

def get(name, var):
    if var in scopes[name]['variables']:
        print(name)
    elif scopes[name]['parent'] == None:
        print(None)
    else: get(name = scopes[name]['parent'], var = var)

n = int(input())
scopes = {'global': {'parent': None, 'variables': set()}}

for i in range(n):
    cmd, name, var = input().split(' ')
    if cmd == 'add':
        add(name, var)
    if cmd == 'create':
        create(name, var)
    if cmd == 'get':
        get(name, var)
        """



# 1.4 Пространства имён и области видимости 9 из 10 шагов пройдено. Not my code

# Пример решения. Будем храним две структуры:
# 1) Кто чей родитель
# 2) Переменные объявленные в данном пространстве имён
# Если команда create -- создаём новое пространство имён (запоминаем родителя и создаём пустое множество переменных,
# объявленных в этом пространстве имен).
# Если команда add -- то просто помещаем имя переменной в соответствующее множество.
# Если команда get -- то проверяем наличие данной переменной в нашем пространстве имён,
# если не нашли: проверяем в родителе. Если не нашли в родителе, проверяем в родителе родителя и так далее.
# Как только нашли имя переменной -- вывели на экран пространство имён, в котором нашли.
# Если в процессе поиска мы имя не нашли (fst is None) -- выводим None на экран.


"""n = int(input())

parent = {"global": None}
vs = {"global": set()}

for _ in range(n):
    t, fst, snd = input().split()
    if t == "create":
        parent[fst] = snd
        vs[fst] = set()
    elif t == "add":
        vs[fst].add(snd)
    else:  # t == get
        while fst is not None:
            if snd in vs[fst]:
                break
            fst = parent[fst]
        print(fst)"""



# 1.4 Пространства имён и области видимости 9 из 10 шагов пройдено. Not my code

# Да, задача для словаря, как и прописали 100 раз в комментариях. :) Поэтому в знак протеста
# принципиально решил через "строковый автомат", который создаёт список с конструкциями типа:
# 'global', 'foo_global', 'a_global', 'b_foo_global', 'bar_foo_global'  и работает с ними.
# Функция build_ns() помогает создавать новую строку нужного формата, вторая функция рекурсивно
# ищет нужную строку в списке, выкусывая поочерёдно из строки нэймспейсы двигаясь к global
# (фактически обращаясь к "родителю"). Не сильно длинее, хотя и не так наглядно :)
# Кстати, таким путём можно не уникальные нэймспейсы создавать.
# решение через строковый автомат

"""namespaces = ['global']
sep = '_'

def build_ns(ns):
    return [i for i in namespaces if i.split(sep)[0] == ns][0]

def find_ns(s):
    if s in namespaces: return s.split(sep)[1]
    elif s.count(sep) == 1: return 'None'
    else: return find_ns(s[:s.find(sep)] + s[s.find(sep, s.find(sep)+1):])

for cmd, nsps, val in [input().split() for i in range(int(input()))]:
    if cmd == 'add': namespaces.append(val + sep + build_ns(nsps))
    if cmd == 'create': namespaces.append(nsps + sep + build_ns(val))
    if cmd == 'get': print(find_ns(val + sep + build_ns(nsps)))"""











######





# 1.5 Введение в классы 7 из 12 шагов пройдено

# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
#
# Каждая копилка имеет ограниченную вместимость, которая выражается
# целым числом – количеством монет, которые можно положить в копилку.
# Класс должен поддерживать информацию о количестве монет в копилке,
# предоставлять возможность добавлять монеты в копилку и узнавать,
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
#
# Класс должен иметь следующий вид
#
# class MoneyBox:
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         # положить v монет в копилку
# При создании копилки, число монет в ней равно 0.
# Примечание:
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.




# 1.5 Введение в классы 7 из 12 шагов пройдено. Correct answer
"""class MoneyBox:
    def __init__(self, capacity, val = 0):
        self.capacity = capacity
        self.val = val
    def can_add(self, v):
        if self.capacity >= self.val + v:
            return True
        return False
    def add(self, v):
        self.val += v"""


# 1.5 Введение в классы 7 из 12 шагов пройдено. Not my code
# Классно написана 2я функция в одну строку

"""class MoneyBox:
    def __init__(self, capacity):
        self.count_coin = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.count_coin + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.count_coin += v"""


# 1.5 Введение в классы 7 из 12 шагов пройдено. Not my code
# Классно, что можно выводить информацию о копилке
# + классное решение с 1 аргументом
"""class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.capacity = self.capacity - v
            return 'В копилке {} монет(ы)'.format(v)
        return 'В копилке есть место только для {} монет(ы)'.format(self.capacity)"""








######







# 1.5 Введение в классы 8 из 12 шагов пройдено


# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран
# сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.
#
# Но последовательность не дается вам сразу целиком. С течением времени
# к вам поступают её последовательные части. Например, сначала первые три элемента,
# потом следующие шесть, потом следующие два и т. д.
#
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности
# и выводить сумму пятерок последовательных элементов по мере их накопления.
#
# Одним из требований к классу является то, что он не должен хранить в себе
# больше элементов, чем ему действительно необходимо, т. е. он не должен хранить элементы,
# которые уже вошли в пятерку, для которой была выведена сумма.
#
# Класс должен иметь следующий вид

# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#
#     def add(self, *a):
#         # добавить следующую часть последовательности
#
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены

# Пример работы с классом

# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]


# 1.5 Введение в классы 8 из 12 шагов пройдено. Correct answer
"""
class Buffer:
    def __init__(self):
        self.buf = []

    def add(self, *a):
        self.buf += a
        for i in range(len(self.buf) // 5):
            print(sum(self.buf[:5]))
            self.buf = self.buf[5:]

    def get_current_part(self):
        return self.buf
"""


# 1.5 Введение в классы 8 из 12 шагов пройдено. Not my code

# Пример правильного решения:
# Атрибут self.part -- хранит текущее состояние нашего буфера.
# Внутри метода add после добавления каждого элемента, проверяем
# длину текущего состоянии нашего буфера: если длина стала равно
# 5 -- выводим на экран сумму элементов в буфере и не забываем чистить буфер.
"""
class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part
"""


# 1.5 Введение в классы 8 из 12 шагов пройдено. Not my code
"""
class Buffer:
    def __init__(self):
        self.buf = []
    def add(self, *a):
        self.buf.extend(a)
        while len(self.buf) >=5:
            print(self.buf.pop(0)+self.buf.pop(0)+self.buf.pop(0)+self.buf.pop(0)+self.buf.pop(0))
    def get_current_part(self):
        return self.buf"""


# 1.5 Введение в классы 8 из 12 шагов пройдено. Not my code

# Немного рекурсии, Богу Рекурсии.
"""
class Buffer:
    def __init__(self):
        self.buffer_list = []

    def add(self, *a):
        for element in a:
            self.buffer_list.append(element)
        self.analyze_buffer()

    def get_current_part(self):
        return self.buffer_list

    def analyze_buffer(self):
        if len(self.buffer_list) >= 5:
            print(sum(self.buffer_list[:5]))
            del self.buffer_list[:5]
            self.analyze_buffer()
"""

