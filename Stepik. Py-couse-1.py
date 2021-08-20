# 2.6 Задачи по материалам недели 7 из 11 шагов пройдено
"""Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно).
На вход программе передаётся неотрицательное целое число n — столько элементов последовательности
должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел
в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4."""

"""a = [1, 2, 3, 4]
print(a)
print([a[0]] * 5)
print(a * 2)

b = []
b = a[1]
print('b =', [b] * 2)"""

"""a = [1, 2, 3, 4]
for i in range(len(a)):
    print([a[i]] * (i + 1))"""

"""a = [1, 2, 3, 4]
b = []
for i in range(len(a)):
    b.append([a[i]] * (i + 1))
    print(b)"""

"""n = 5
a = [[0 for j in range(n)] for i in range(n)]
print(a)"""

""" n = 5
f = 1
b = 1

for j in  range(n):
    a = [b for i in range(f)]
    b += 1
    f += 1
    print(a)"""

"""n = 5
f = 1
b = 1
c = []

for j in  range(n):
    a = [b for i in range(f)]
    b += 1
    f += 1
    c.append(a)
print(*c)
print(len(c))
print(list(c))"""

""" 
n = 7
a = 1
for i in range(n):
    print(a, end=' ')"""

# 2.6 Задачи по материалам недели 7 из 11 шагов пройдено. Correct answer
"""n = int(input())
a = 1
b = []
for i in range(n):
    for j in range(a):
        b.append(a)
    a += 1
print(*b[:n])"""

# 2.6 Задачи по материалам недели 7 из 11 шагов пройдено. Not my code
"""i, n, s = 1, int(input()), []
while len(s) < n:
    s += [i] * i
    i += 1
print(*s[:n])

a = int(input())

b = []"""

# 2.6 Задачи по материалам недели 7 из 11 шагов пройдено. Not my code
"""for i in range(1, a + 1):
    b += [i] * i

print(*b[0:a])"""

# 2.6 Задачи по материалам недели 8 из 11 шагов пройдено
"""Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, 
которая выводит все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, 
вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения."""

"""
lst = [int(i) for i in input().split()]
a = int(input())
"""

"""
while b < 10:
    b = lst.index(a)
    print(b, end=', ')
    b += 1

print(lst.index(8))
"""

# 2.6 Задачи по материалам недели 8 из 11 шагов пройдено. Correct answer
"""
lst = [int(i) for i in input().split()]
a = int(input())
b = 0

if lst.count(a) == 0:
    print('Отсутствует')
else:
    f = lst.index(a)
    for i in range(lst.count(a)):
        print(lst.index(a, f), end=' ')
        f = lst.index(a, f)
        f += 1
"""

# 2.6 Задачи по материалам недели 8 из 11 шагов пройдено. Correct answer
"""
l = [int(i) for i in input().split()]
x = int(input())
if not x in l: print('Отсутствует')
for i in range(len(l)):
    if l[i]==x: print(i, end = ' ')
"""

# 2.6 Задачи по материалам недели 9 из 11 шагов пройдено
"""Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. 
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, 
у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы 
на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению."""

"""lst = [[int(j) for j in input().split()] int(i)
for i in input().split()]"""

"""a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for i in a:
    for j in i:
        print(j, end=' ')
    print()"""

"""while int(input()) != 'end':
    for i in int(input()):
        b = []
        for j in int(input()):
            b.append(int(input()))
        a.append(b)"""

"""if int(input()) != 'end':
    l = [int(i) for i in input().split()]
    print(l)
    f = [int(i) for i in input().split()]
    print(f)
    t = [int(i) for i in input().split()]
    print(t)
    print(l, f, t)
else:
    print('this is the end')"""

# 3 STEP
# 3.1 Функции 2 из 9 шагов пройдено

"""def f(n):
    return n * 10 + 5
print(f(f(f(10))))"""

# 3.1 Функции 7 из 9 шагов пройдено
"""Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
1−(x+2)2 при x≤−2
- x/2 при −2<x≤2
1+(x-2)2 при x<2
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода."""

# 3.1 Функции 7 из 9 шагов пройдено. Correct answer
"""def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    elif x > 2:
        return 1 + (x - 2) ** 2"""

# 3.1 Функции 7 из 9 шагов пройдено. Not my code
"""def f(x):
    return {
        x <= -2:      1 - (x + 2) ** 2,
        -2 < x <= 2:  -x / 2,
        2 < x:        (x - 2) ** 2 + 1
    }[True]"""

# 3.1 Функции 8 из 9 шагов пройдено
"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, 
удаляет из него все нечётные значения, а чётные нацело делит на два. 
Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

Функция не должна осуществлять ввод/вывод информации.
"""

"""def modify_list(l):
    l = [2, 3, 4, 6, 4, 7]
    ml = []
    for i in l:
        if i // 2 != 0:
            del l[i]
        elif i // 2 == 0:
            i = i // 2
            ml += [i]
    print(ml)"""

"""l = [2, 3, 4, 6, 4, 7]
ml = []
for i in l:
    if i % 2 == 1:
        del l[i]
    elif i % 2 == 0:
        i = i // 2
        ml += [i]
print(ml)"""

"""
l = [10, 5, 8, 3]
ml = []
f = len(l)
for i in l:
    if i % 2 == 0:
        i = i // 2
        ml += [i]
print(ml)
print(l)
del l[0:f]
l = ml
print(l)
print(f)
"""

# 3.1 Функции 8 из 9 шагов пройдено. Correct answer
"""
def modify_list(l):
    ml = []
    f = len(l)
    for i in l:
        if i % 2 == 0:
            i = i // 2
            ml += [i]
    del l[0:f]

    for i in ml:
        l.append(i)
    return l

l = [10, 5, 8, 3]
modify_list(l)
print('hi', l)
"""

# 3.1 Функции 8 из 9 шагов пройдено. Not my code
"""
def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]
"""

# 3.1 Функции 8 из 9 шагов пройдено. Not my code
"""
def modify_list(l):
    for x in l[:]:
        if x % 2 == 0:
            l.append(x//2)
        l.remove(x)
"""

# 3.1 Функции 8 из 9 шагов пройдено. Not my code
"""
def modify_list(l):
    l[:] = [i//2 for i in l if i % 2 == 0]
"""
"""присвоить элементам из l новые значения по следующему правилу : 
если число в исходном списке чётное, то поделить его пополам.

таким образом, для нечётных мы ничего не делаем и они не попадают в итоговый список."""

# 3.1 Функции 8 из 9 шагов пройдено. Not my code
"""
def modify_list(l):
    b = []
    for x in l:
        if x % 2 == 0:
            b.append(x // 2)
    l[:] = b
"""
"""Используется интересный способ по изменению элементов массива 
через присваивание элементов из нового массива b в исходный l."""

# 3.1 Функции 8 из 9 шагов пройдено. Not my code
"""
def modify_list(l):
    for i in range(len(l)):
        if l[i] != 0 and l[i] % 2 == 1:
            l[i] = "aaa"
        else:
            l[i] = l[i] // 2

    while "aaa" in l:
        l.remove("aaa")
"""
"""Мне надоело учитывать сдвиги списка при удалении, и я сделала жульничество: 
пометила элементы-кандидаты на удаление строкой "aaa", а после прохода списка удалила их...

PS. Как выяснилось: этот же код прекрасно работает, если например заменить строку "aaa" на None."""

# 3.2 Словари 1 из 7 шагов пройден

# Справка
"""
List - Элементы в списке хранятся последовательно, каждому из них присвоены индексы, начиная с нуля.
Turple - Кортеж, неизменяемый и более быстрый аналог списка.
Set - Множество, набор уникальных элементов в случайном порядке (неупорядоченный список)."""

# Ещё раз подробно про генераторы
"""
Когда использовать List Comprehension в Python
https://webdevblog.ru/kogda-ispolzovat-list-comprehension-v-python/
"""

# 3.2 Словари 4 из 7 шагов пройдено

""""
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь 
d и два числа: key и value

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 
2∗key. Если и ключа 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента 
[value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}

"""

"""
def update_dictionary(d, key, value):
    d = {}
    """
"""
d = {1: 2, 'a': 10, 33: [1, 3, 7]}
print(d)
print(d[1], d['a'], d[33], sep=', ')
print(d[33][2], d[33][1])
d[1] = 4
print(d)
d[33][1] = 50
print(d)
d[33].append(12)
print(d)
d["wooo"] = 23
print(d)
"""

"""d = {2: [1, 2, 4], 15: [1, 23]}
key = 3
value = -1"""

# 3.2 Словари 4 из 7 шагов пройдено. Correct answer
"""
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key not in d:
        key2 = 2 * key
        if key2 in d:
            d[key2].append(value)
        else:
            d[key2] = [value]
"""

# 3.2 Словари 4 из 7 шагов пройдено. Not my code

"""
True -> 1

False -> 0
"""

"""
def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]
"""
"""
ВОПРОС:
Зачем было добавлено?
...=d.get(key, [])+...

Разве не достаточно просто написать?
d[key]=[value]

ОТВЕТ:
Тогда предыдущий список просто заменится на новый [value]. 
Нельзя и d[key].append(value) (или + [value]), т.к. будет ошибка, 
если в словаре нет пока ключа key. Вызов get(key, []) создаёт в этом случае ключ и 
приписывает ему пустое значение, если же ключ уже есть, то просто возвращает значение по ключу 
(предполагается, что словарь заполняется нашей ф-цией и там могут быть только списки.  Д
ля понимания можно потестить код:
dic = {}
dic[1] = dic.get(1, []) + [1, 2] #попробуйте заменить эту строку на:  dic[1].append( [1, 2] )
dic[1] = [3]
print(dic)
Извините, за подробности, но исходя из вопроса я понял, что требуется именно такой ответ, 
хотя автор решения его бы непременно оптимизировал не в ущерб смыслу. :)


get(key) по умолчанию возвращает None если ключа нет в списке. 
Но вы можете изменить это значение передав его в функцию через запятую после значения ключа 
(по аналогии с функцией range() ) get(key, value).

В данном случае он меняет None на пустой список []. 
В случае, если такого ключа не будет в словаре, то функция get вернет не None, а вернет пустой список. 
Следовательно, у нас появится ключ key, которому будет соответствовать значение [] (т.е пустой список).
"""

# 3.2 Словари 4 из 7 шагов пройдено. Not my code
"""
def update_dictionary(d, key, value): d.setdefault(key+key*(key not in d),[]).append(value)

1. setdefault проверяет, есть ли key в словаре d. Если есть, то далее работаем с ключом key, 
если нет - далее работаем с удвоенным key.

2. setdefault проверяет, есть ли выбранный ключ в словаре d. 
Если есть - то возвращает список, хранящийся по этому ключу. Если нет - создаёт пустой список.

3. append добавляет к этом списку новое значение - value.

4. Обновив список, update_dictionary просто возвращает None.
"""

# 3.2 Словари 5 из 7 шагов пройдено
"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и 
в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, 
разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить 
для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
в формате "слово количество" (см. пример вывода). 
Порядок вывода слов может быть произвольным, 
каждое уникальное слово должно выводиться только один раз.
"""

"""
f = 'asdfSSS'
f = f.lower()
print(f)

for i in range(len(d)):
    d[i] = d[i].lower()
    print(d)
print(d)
"""
"""
c = 0
for i in range(len(d)):
    c = 0
    if d[i] in d:
        c += 1
    print(d[i], c)
"""

"""d = ['a', 'aa', 'abC', 'Aa', 'ac', 'abc', 'bcd', 'a']
f = []
for i in range(len(d)):
    d[i] = d[i].lower()
print(d)

for i in range(len(d)):
    c = d.count(d[i])
    print(d[i], c)
    f.append(d[i])
    f.append(c)
    print(f)
f = set(f)
print(*f)"""

"""lst = ['a', 'aa', 'abC', 'Aa', 'ac', 'abc', 'bcd', 'a']
lst = ['a', 'A', 'a']"""

# 3.2 Словари 5 из 7 шагов пройдено. Correct answer
"""
lst = [i for i in input().split()]
dict = {}

for i in range(len(lst)):
    lst[i] = lst[i].lower()

for i in lst:
    c = lst.count(i)
    dict[i] = c

for key, value in dict.items():
    print(key, value)
"""

# 3.2 Словари 5 из 7 шагов пройдено. Not my code
"""s = input().lower().split()
for i in set(s):
    print(i, s.count(i))"""

# 3.2 Словари 5 из 7 шагов пройдено. Not my code
"""x = [i for i in input().lower().split()]
a = {i:x.count(i)for i in x}
for i,j in a.items():
  print(i,j)"""

# 3.2 Словари 5 из 7 шагов пройдено. Not my code
"""l = input().lower().split()
d  = {e:0 for e in l} #создаем словарь на основе списка с 0 значениями
for key in l: d[key]+= 1 #тупо считаем повторяющиеся
for key,value in d.items(): print(key, value) #тупо выводим"""

# 2.4 Строки и символы 6 из 7 шагов пройдено
"""
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт 
биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, 
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов 
исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит 
закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
"""

"""print(s)
cnt = 0
for i in range(len(s)):
    if s[i] == s[i+1]:
        cnt += 1
    print(s[i], cnt, end='')"""

"""s = 'aaaabbсaa'
cnt = 1

for i in s:
    cnt = 1
    if i == s[cnt]:
        cnt += 1
    else: print(i,cnt)"""
"""
s = 'aaaabbсaa'
cnt = 1

for i in s:
    cnt = 1
    while i == s[cnt]:
        cnt += 1
    else: print(i,cnt, sep='', end=' ')
"""

"""
for i in range(len(s)):
    cnt = 1
    a = 1
    while s[i] != s[i + a]:
        cnt += 1
        a += 1
    else:
        print(s[i], cnt, sep='', end=' ')
"""

"""s = 'aaaabbсaa'
f = 0

for i in range(len(s)):
    cnt = 1
    a = 1

    while s[i + f] == s[i + a]:
        cnt += 1
        a += 1
    else:
        print(s[i], cnt, sep='', end=' ')
"""

"""
s = 'aaaabbсaa'
f = 0

for i in range(len(s)):
    cnt = 1
    a = 1
    i = 0

    while s[i + f] == s[i + f + a]:
        cnt += 1
        a += 1
    else:
        if cnt >= 1:
            print(s[i + f], cnt, sep='', end=' ')
            f += cnt
"""

"""
s = 'aaaabbсaa'
f = 0
cnt = 1
a = 1

for i in range(len(s)):
    i = 0
    if (i + f + a) > len(s) - 1:
        break

    cnt = 1
    a = 1

    while s[i + f] == s[i + f + a]:
        cnt += 1
        a += 1
        if (i + f + a) > len(s) - 1:
            print(s[i + f], cnt, sep='', end='')
            break
    else:
        if cnt >= 1:
            print(s[i + f], cnt, sep='', end='')
            f += cnt
            """

"""
s = 'aaaabbсaa'
#s = 'abc'
#s = 'neeeeeeea'
f = 0
cnt = 1
a = 1

for i in range(len(s)):
    i = 0
    if (i + f + a) > len(s) - 1:
        if cnt >= 1:
            print(s[-1], 1, sep='', end='')
        break


    cnt = 1
    a = 1

    while s[i + f] == s[i + f + a]:
        cnt += 1
        a += 1
        if (i + f + a) > len(s) - 1:
            print(s[i + f], cnt, sep='', end='')
            break
    else:
        print(s[i + f], cnt, sep='', end='')
        f += cnt
        """

"""
#s = 'aaaabbсaa'
#s = 'abc'
# s = 'neeeeeeea'
# s = 'ROBb'
s = 'neeebba'
f = 0
cnt = 1
a = 1
stop = 0
for i in range(len(s)):
    if stop != 1:

        i = 0
        if (i + f + a) > len(s) - 1:
            if cnt >= 1:
                print(s[-1], 1, sep='', end='')
                stop = 1
            break

        cnt = 1
        a = 1
        if stop != 1:
            while s[i + f] == s[i + f + a]:
                cnt += 1
                a += 1
                if (i + f + a) > len(s) - 1:
                    print(s[i + f], cnt, sep='', end='')
                    stop = 1
                    break
            else:
                print(s[i + f], cnt, sep='', end='')
                f += cnt
                """

"""
#s = 'aaaabbсaa'
#s = 'abc'
# s = 'neeeeeeea'
# s = 'ROBb'
s = 'neeebba'
f = 0
cnt = 1
a = 1
stop = 0
for i in range(len(s)):
    if stop != 1:

        i = 0
        if (i + f + a) > len(s) - 1:
            if cnt >= 1:
                print(s[-1], 1, sep='', end='')
                stop = 1
            break

        cnt = 1
        a = 1
        if stop != 1:
            while s[i + f] == s[i + f + a]:
                cnt += 1
                a += 1
                if (i + f + a) > len(s) - 1:
                    print(s[i + f], cnt, sep='', end='')
                    stop = 1
                    break
            else:
                print(s[i + f], cnt, sep='', end='')
                f += cnt
"""

"""
#s = 'aaaabbсaa'
#s = 'abc'
# s = 'neeeeeeea'
# s = 'ROBb'
s = 'neeebba'

f = 0
a = 1
cnt = 1

while (f + a) <= len(s):
    while s[f] == s[f + a]:
        cnt += 1
        a += 1
    else:
        print(s[f], cnt, sep='', end='')
        f += cnt
"""

"""
s = 'aaaabbсaa'
#s = 'abc'
# s = 'neeeeeeea'
# s = 'ROBb'
# s = 'neeebba'

f = 0
cnt = 1

while (f + 1) < len(s):
    cnt = 1
    while s[f] == s[f + 1]:
        cnt += 1
        f += 1
    else:
        print(s[f], cnt, sep='', end='')
        f += 1
else:
    f = 1
    while s[-1] == s[-1 - f]:
        cnt += 1
        f += 1
    else:
        print(s[-f], cnt, sep='', end='')
        f += 1"""

"""        if (f + 1) >= len(s) - 1:
            print(s[-1], 1, sep='', end='')
            break"""

"""while (f + 1) <= len(s):
    cnt = 1
    while s[f] == s[f + 1]:
        cnt += 1
        f += 1
    else:
        print(s[f], cnt, sep='', end='')
        f += 1"""

"""
s = input()
f = 0
cnt = 1

while (f + 1) < len(s):
    cnt = 1
    while s[f] == s[f + 1]:
        cnt += 1
        f += 1
    else:
        print(s[f], cnt, sep='', end='')
        f += 1"""

"""
# s = 'aaaabbсaa'
# s = 'abc'
# s = 'neeeeeeea'
# s = 'ROBb'
# s = 'neeebba'
s = 'ssssssssss'
f = 0
cnt = 1

while (f + 1) < len(s):
    cnt = 1
    while s[f] == s[f + 1]:
        cnt += 1
        f += 1
        if (f + 1) >= len(s):
            break
    else:
        print(s[f], cnt, sep='', end='')
        f += 1
else:
    f = 1
    cnt = 1
    while s[-1] == s[-1 - f]:
        cnt += 1
        f += 1
    else:
        print(s[-f], cnt, sep='', end='')
        f += 1
"""

# 2.4 Строки и символы 6 из 7 шагов пройдено. Correct answer!!!!!!! BLYAAAT!
"""
# s = 'aaaabbсaa'
# s = 'abc'
# s = 'neeeeeeea'
# s = 'ROBb'
# s = 'neeebba'
# s = 'ssssssssss'
s = 'a'

f = 0
cnt = 1

if len(s) == 1:
    print(s, 1, sep='', end='')
else:
    while (f + 1) < len(s):
        cnt = 1
        while s[f] == s[f + 1]:
            cnt += 1
            f += 1
            if (f + 1) >= len(s):
                break
        else:
            print(s[f], cnt, sep='', end='')
            f += 1
    else:
        f = 1
        cnt = 1
        while s[-1] == s[-1 - f]:
            cnt += 1
            f += 1
            if (f + 1) >= len(s):
                print(s[f], cnt + 1, sep='', end='')
                break
        else:
            print(s[-f], cnt, sep='', end='')
            f += 1
            """

# 2.4 Строки и символы 6 из 7 шагов пройдено. Not my code
"""
genome = input()+' '
s = 0
n=genome[0]         # n = первый элемент в повторяющейся последовательности, для первого элемента строки это верно.
for i in genome:    # текущий элемент всегда i
    if n != i:      # в цикл попадаем, когда первый элемент повторяющихся элементов не совпадёт со следующим элементом
        print(n + str(s), end = '')
        s = 0       # инициализируем длину для новой повторяющейся последовательности = 0
        n = i       # новая последовательность начинается с нового элемента, запишем его в n
    s += 1          # мы сдвинулись на 1 элемент, поэтому увеличиваем последовательность элементов на 1.
"""

# 2.4 Строки и символы 6 из 7 шагов пройдено. Not my code
"""
dna = input()                    # считываем строку
print(dna[0],end='')             # выводим первый символ
cnt = 1                          # счетчик символов на единице
for i in range(0,len(dna)-1):    # итератор проходит по всем индексам символов кроме предпоследнего
    if dna[i] == dna[i+1]:       # сравниваем символ по текущему индексу со следующим
        cnt+=1                   # если символы одинаковые, то увеличиваем счетчик
    else :
        print(cnt,end='')        # если разные, то выводим значение счетчика
        print(dna[i+1],end='')   # выводим следующий символ
        cnt = 1                  # счетчик текущего символа на единице
print(cnt)                       # в конце распечатываем значение счетчика последнего символа
"""

# 3.2 Словари 6 из 7 шагов пройдено

# Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел,
# которые нужно считать. Далее считывает n строк с числами xi, по одному числу в каждой строке.
# Итого будет n+1 строк.
#
# При считывании числа xi программа должна на отдельной строке вывести значение
# f(xi). Функция f(x) уже реализована и доступна для вызова.
#
# Функция вычисляется достаточно долго и зависит только от переданного аргумента
# x. Для того, чтобы уложиться в ограничение по времени,
# нужно избежать повторного вычисления значений.


# 3.2 Словари 6 из 7 шагов пройдено. Correct answer
"""
def f(x):
    return x + 1

n = int(input())
d = {}
for xi in range(n):
    xi = int(input())
    if xi not in d:
        d[xi] = f(xi)
        print(d[xi])
    else: print(d[xi])
"""

# 3.2 Словари 6 из 7 шагов пройдено. Not my code
# Через генераторы
"""
a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])
    """



















# 3.4 Файловый ввод/вывод 1 из 4 шагов пройден.
# На прошлой неделе мы сжимали строки, используя кодирование повторов.
# Теперь нашей задачей будет восстановление исходной строки обратно.
#
# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
#
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
#
# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz"
# у вас появляется ссылка "download your dataset".
# Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
# Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл,
# который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

# Sample Input: a3b4c2e10b1
# Sample Output: aaabbbbcceeeeeeeeeeb


"""
s = 'a3b4c2e10b1'
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = '1234567890'
key = ''
digit = 0

for i in s:
    if i not in numbers:
        key = i
    else:
        digit = int(i)
        print(key * digit)
        """


"""
s = 'a3b4c2e10b1'
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = '1234567890'
key = ''
digit = 0

for i in s:
    if i in numbers:
        digit = int(i)
        print(key * digit)
    else:
        key = i
        """


"""
s = 'i1v16x2E19l3B17q2E15k19l3o12D11V17T11G14g5D14Q15E19v9i5s13r5c6h9J20K20d11b14V1 '
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = '1234567890'
key = ''
digit = 0

for i in range(len(s)):
    if s[i] not in numbers:
        key = s[i]
    else:
        if s[i + 1] not in numbers:
            digit = int(s[i])
            print(key * digit, end='')
        else:
            print(key * int(s[i] + s[i+1]))
"""

"""
# s = 'a3b4c2e10b1 '
s = 'G9f10b9f16Y5m18g10U15J4l20u9 '
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = '1234567890'
key = ''
digit = 0
cnt = 0

for i in s:
    cnt += 1
    if i in numbers:
        digit = int(i)
        if s[cnt] in numbers:
            digit = int(i+s[cnt])
        print(key * digit, end='')
    else:
        key = i
"""

# 3.4 Файловый ввод/вывод 1 из 4 шагов пройден. Correct answer
"""
# s = 'a3b4c2e10b1 '
s = 'c1d1ccc '
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# with open('/Users/nabal/Downloads/dataset_3363_2-4.txt', 'r') as dataset:
#     s = dataset.readline()

numbers = '1234567890'
key = ''
cnt = 0

for i in s:
    cnt += 1

    if i not in numbers:
        key = i
        add = ''
        digit = ''

    else:
        if i in numbers and s[cnt] in numbers:
            add = i
            digit += add
        else:
            digit += i
            print(key * int(digit), end='')
"""


# 3.4 Файловый ввод/вывод 1 из 4 шагов пройден. Not my code
"""
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()


for i in range(len(s)):
    r = 1
    number=''
    if s[i].isalpha():
        while s[i+r].isdigit():
            number += str(s[i + r])
            r+=1
        for _ in range(int(number)):
            print(s[i],end='')

Тут всё достаточно прозрачно. Работа идёт с инкрементированием (к слову, инкремент - хороший костыль во многих случаях, рекомендую!).
1. Перебираем каждый символ строки, с каждым новым перебором задаём тот самый инкремент r и пустую строку number (где r отвечает за проход от текущего элемента в итерации (элемента s[i] ) ровно на 1 элемент вперед, а number - за число, на которое нужно умножить нашу букву)
2. Работая ищейкой, r посимвольно вынюхивает, являются ли элементы за s[i] (которое у нас буква) digit-ами. Если так, то в number записывается число после s[i] до тех пор, пока элемент s[i+r] станет НЕdigit (в нашем случае - alpha).
3. Цикл while заканчивает свою работу, вступает цикл for, который записывает s[i]-ую букву ровно number раз.
4. Самый первый цикл for идёт дальше по элементам нашей строки и применяет вышеназванные пункты только к ALPHA-элементам ( if s[i].isalpha() ), в ином случае, итерация цикла переходит к следующему символу строки s
5. Вуаля!
"""

# 3.4 Файловый ввод/вывод 1 из 4 шагов пройден. Not my code
"""
import re                         #подгрузил библиотеку с регулярными выражениями, рекомендую прочитать статью
                                  #объявил пустую строку в которую в конце буду все записывать
with open("dataset_3363_2.txt") as file:   #открываю файл
  line = file.readline().strip()           #читаю строку
bukvi = re.findall(r'\D', line)             #re.findall находит все сочетания до цифры и помещает их в список в
                                            # #виде ('a', 'A', 'c'...)
                                            #\d - Любая цифра [0-9] (\D — все, кроме цифры)
cifri = re.findall(r'\d+', line)            #\d находит все сочетания цифр, а остальные пропускает, но чтобы он не
                                           #оставлял пробелы вместо пропущенных букв написано '\d+' - где +
                                              #обозначает 1 и более вхождений цифр (по умолчанию, как я понял 0 и
                                           #более вхождений)
for i in range(len(bukvi)):                #поскольку букв и сочетаний цифр одинаковое количество, то цикл
                                           #имеет одинаковую длину (len(bukvi)) как для цифр, так и для букв 
    vyvod+= str(bukvi[i])*int(cifri[i])    #каждую букву записываю в строку определенное количество раз
with open("textfile_out.txt", "w") as outfile: outfile.write(vyvod) #записываю в файл

"""

# 3.4 Файловый ввод/вывод 1 из 4 шагов пройден. Not my code
"""
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j
"""

# 3.4 Файловый ввод/вывод 1 из 4 шагов пройден. Not my code
"""
s, d = input(), []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')
"""













# 3.4 Файловый ввод/вывод 2 из 4 шагов пройдено

# Недавно мы считали для каждого слова количество его вхождений в строку.
# Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
#
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
#
# В качестве ответа укажите вывод программы, а не саму программу.
#
# Слова, написанные в разных регистрах, считаются одинаковыми.


# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3

"""# lst = ['abc', 'a', 'bCd', 'bC', 'AbC', 'BC', 'BCD', 'bcd', 'ABC']
lst = ['abc', 'aac', 'bCd', 'bC', 'AbC', 'BC', 'BCD', 'bcd', 'ABC', 'aac', 'aac']
dict = {}
maxx = 0

for i in range(len(lst)):
    lst[i] = lst[i].lower()

for i in lst:
    c = lst.count(i)
    dict[i] = c
    if c > maxx:
        maxx = c
        key = i

print(key, dict[key])
print()
for key, value in dict.items():
    print(key, value)"""



"""
# lst = ['abc', 'a', 'bCd', 'bC', 'AbC', 'BC', 'BCD', 'bcd', 'ABC']
lst = ['abc', 'aac', 'bCd', 'bC', 'BC', 'BCD', 'bcd', 'ABC', 'aac', 'aac', 'AbC']
dict = {}
maxx = 0
key = 'z'

for i in range(len(lst)):
    lst[i] = lst[i].lower()

for i in lst:
    c = lst.count(i)
    dict[i] = c
    if c >= maxx:
        if key > i:
            maxx = c
            key = i

print(key, dict[key])
print()
for key, value in dict.items():
    print(key, value)"""


# with open('/Users/nabal/Downloads/dataset_3363_2-4.txt', 'r') as dataset:
#     s = dataset.readline()


# lst = ['abc', 'a', 'bCd', 'bC', 'AbC', 'BC', 'BCD', 'bcd', 'ABC']
# lst = ['abc', 'aac', 'bCd', 'bC', 'BC', 'BCD', 'bcd', 'ABC', 'aac', 'aac', 'AbC']





# 3.4 Файловый ввод/вывод 2 из 4 шагов пройдено. Correct answer

"""
def FindMaxCount(line):
    lst = line
    dict = {}
    maxx = 0
    key = 'z'

    for i in range(len(lst)):
        lst[i] = lst[i].lower()

    for i in lst:
        c = lst.count(i)
        dict[i] = c
        if c >= maxx:
            if key > i:
                maxx = c
                key = i


    return key, dict[key]


FullText = []
with open('/Users/nabal/Downloads/dataset_3363_3-2.txt', 'r') as dataset:
    for line in dataset:
        # FullText.append(line.strip().split(' '))
        FullText += line.strip().split(' ')
    print(FullText)
    print(*FindMaxCount(FullText))
"""



# 3.4 Файловый ввод/вывод 2 из 4 шагов пройдено. Not my code

"""with open('/Users/nabal/Downloads/Bibliya__Bibliya_www.Litmir.net_283.txt') as inf, open('/Users/nabal/Downloads/Bible_txt.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))


Без словаря короче и красивее, но одни и те же слова программа считает несколько раз, поэтому медленнее.

@Никита_Иванов, еще вот так добавить, и вообще красота -  for word in set(s):
чтобы одинаковые не обрабатывать по несколько раз.

@Сергей_Смирнов, нет, set()  изменит список и он перестанет быть отсортированным.
То-есть в примере: " aa Bb F cc" должен быть ответ "aa" но выдаст "cc ".
Но можно отсортировать таким образом и будет правильно: "sorted( set(s) )"""



# 3.4 Файловый ввод/вывод 2 из 4 шагов пройдено. Not my code
"""
s, d, m, w = str(), dict(), 0, str()
with open("/Users/nabal/Downloads/Bibliya__Bibliya_www.Litmir.net_283.txt", "r") as f:
    s = f.read().lower().strip().split()
s.sort()
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > m:
        m = d[word]
        w = word
"""

# 3.4 Файловый ввод/вывод 2 из 4 шагов пройдено. Not my code
"""@Liudmila_Ageeva, вы абсолютно правы. Чтобы это исключить, нужно вызвать метод сттроки replace, вот так:
from collections import Counter

with open('Bible.txt', 'r') as file:
    words = [i.lower() for i in file.read().replace(';', '').replace(',', '').replace(':', '').split()]

most_common = Counter(words).most_common(1)[0]
print(*most_common)"""


# 3.4 Файловый ввод/вывод 2 из 4 шагов пройдено. Not my code
"""
def CountWord(d, key, value):
    if key in d:
        d[key] += 1
    else:
        d[key] = value

s1 = []
with open('D:\python\\bibl.txt', 'r') as text:
    for line in text:
        L = line.lower().strip().split()
        s1.extend(L)
s1.sort()

dict_of_word = {}
for word in s1:
    CountWord(dict_of_word, word, 1)

max_q = 0
first_word = ''
for word, q in dict_of_word.items():
    if q > max_q:
        max_q = q
        first_word = word
print(first_word, max_q)"""











# 3.4 Файловый ввод/вывод 3 из 4 шагов пройдено

# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
# где в каждой строке записана следующая информация:
#
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#
# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента
# записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом.
#
# Также вычислите средние баллы по математике, физике и русскому языку
# по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.
#
# В качестве ответа на задание прикрепите полученный файл со средними
# оценками по каждому ученику и одной строкой со средними оценками по трём предметам.
#
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']
#
# Sample Input:
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
#
# Sample Output:
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667


# 3.4 Файловый ввод/вывод 3 из 4 шагов пройдено. Correct answer
"""
bigList = []
with open('/Users/nabal/Downloads/dataset_3363_4-2.txt', 'r') as data:
    # data = data.readline().strip().split(';')
    for line in data:
        bigList += [line.strip().split(';')]

sums1, sums2, sums3 = 0, 0, 0
for i in bigList:
    sums1 += int(i[1])
    sums2 += int(i[2])
    sums3 += int(i[3])
print(sums1 / len(bigList), sums2 / len(bigList), sums2 / len(bigList))


with open('/Users/nabal/Downloads/Bible.txt', 'w') as ouf:
    for i in bigList:
        ouf.write(str((int(i[1]) + int(i[2]) + int(i[3])) / 3))
        ouf.write('\n')
with open('/Users/nabal/Downloads/Bible.txt', 'a') as ouf:
    ouf.write(str(sums1 / len(bigList)))
    ouf.write(' ')
    ouf.write(str(sums2 / len(bigList)))
    ouf.write(' ')
    ouf.write(str(sums3 / len(bigList)))
"""

# 3.4 Файловый ввод/вывод 3 из 4 шагов пройдено. Not my code
"""koll, a1, b1, c1 = 0, 0, 0, 0
with open('dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        line = line.strip().split(';')
        a, b, c = int(line[1]), int(line[2]), int(line[3])
        print((a+b+c)/3)
        koll += 1
        a1 += a
        b1 += b
        c1 += c
print((a1/koll), (b1/koll), (c1/koll))"""
























# 3.5 Модули, подключение модулей 1 из 3 шагов пройден
# Напишите программу, которая подключает модуль math и, используя значение числа
# π из этого модуля, находит для переданного ей на стандартный ввод радиуса круга
# периметр этого круга и выводит его на стандартный вывод.
#
# Sample Input:
# 10.0
#
# Sample Output:
# 62.83185307179586

# 3.5 Модули, подключение модулей 1 из 3 шагов пройден. Correct answer
"""
import math
r = float(input())
print(2 * math.pi * r)
"""

# from math import pi as pipipipi

# from math import tau
# print(float(input()) * tau)







# 3.5 Модули, подключение модулей
# Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран
# (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
#
# Для доступа к аргументам командной строки программы подключите модуль sys и
# используйте переменную argv из этого модуля.
#
#
# Пример работы программы:
# > python3 my_solution.py arg1 arg2
# arg1 arg2

# 3.5 Модули, подключение модулей. Correct answer
"""from sys import argv
print(*argv[1:])"""
















# 3.6 Установка дополнительных модулей 1 из 3 шагов пройден

# Скачайте файл. В нём указан адрес другого файла, который нужно скачать
# с использованием модуля requests и посчитать число строк в нём.
#
# Используйте функцию get для получения файла (имеет смысл вызвать метод strip
# к передаваемому параметру, чтобы убрать пробельные символы по краям).
#
# После получения файла вы можете проверить результат, обратившись к полю text.
# Если результат работы скрипта не принимается, проверьте поле url на правильность.
# Для подсчёта количества строк разбейте текст с помощью метода splitlines.
#
# В поле ответа введите одно число или отправьте файл, содержащий одно число.



# 3.6 Установка дополнительных модулей 1 из 3 шагов пройден. Correct answer
"""with open('/Users/nabal/Downloads/dataset_3378_2-2.txt', 'r') as data:
    url = data.readline().strip()
    print(url)

from requests import get
# r = get('https://stepic.org/media/attachments/course67/3.6.2/168.txt')
r = get(url)
print(r.text)
print(len(r.text.splitlines()))
print(len(r.text))"""


# 3.6 Установка дополнительных модулей 1 из 3 шагов пройден. Not my code
"""
Два представления решения: читабельный и для любителей извращений)

from requests import get
with open('dataset.txt') as f:
    url = f.readline().strip()
text = get(url).text.splitlines()
print(len(text))


import requests
print(len(requests.get(open('dataset.txt').readline().strip()).text.splitlines()))"""


















# 3.6 Установка дополнительных модулей 2 из 3 шагов пройдено

# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое последнего файла из набора, как ответ на это задание.


# 3.6 Установка дополнительных модулей 2 из 3 шагов пройдено. Correct answer
"""
from requests import get

a = 'balalaika'
r = get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while a != 'We':
    r = get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
    print(r.text)
    if 'We' in r.text.split(' '):
        a = 'We'
"""















# 3.7 Задачи по материалам недели 0 из 5 шагов пройдено

# Напишите программу, которая принимает на стандартный вход список игр футбольных
# команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.

# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


# d = {}
# lst = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]
# d['team'] = lst[0]
# d['numGames'] = 0
# d['wins'] = lst[1]
# d['draws'] = 0
# d['looses'] = 0
# d['points'] = 0
#
# print(d)

"""
d = {}
numGames = {}
wins = {}
draws = {}
defeats = {}
points = {}

lst = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]
teamlst = []
lst = [i for i in input().split(';')]

for i in lst:
    numGames[i[0]], numGames[i[2]] = 0, 0
    wins[i[0]], wins[i[2]] = 0, 0
    draws[i[0]], draws[i[2]] = 0, 0
    defeats[i[0]], defeats[i[2]] = 0, 0
    points[i[0]], points[i[2]] = 0, 0

for i in range(len(lst)):
    teamlst.append(lst[i][0])
    teamlst.append(lst[i][2])

for i in lst:
    numGames[i[0]] += 1
    numGames[i[2]] += 1

    if int(i[1]) > int(i[3]):
        wins[i[0]] += 1
        defeats[i[2]] += 1
        points[i[0]] += 3
    elif int(i[1]) == int(i[3]):
        draws[i[0]] += 1
        draws[i[2]] += 1
        points[i[0]] += 1
        points[i[2]] += 1
    elif int(i[1]) < int(i[3]):
        wins[i[2]] += 1
        defeats[i[0]] += 1
        points[i[2]] += 3


# print('Всего игр: ', end='')
# print(numGames)
# print('Побед: ', end='')
# print(wins)
# print('Ничьих: ', end='')
# print(draws)
# print('Поражений: ', end='')
# print(defeats)
# print('Всего очков: ', end='')
# print(points)
#
# print(teamlst)
# print(set(teamlst))

for i in set(teamlst):
    print(i, ': ', numGames[i], ' ', wins[i], ' ', draws[i], ' ', defeats[i], ' ', points[i], sep='')

"""





"""d = {}
numGames = {}
wins = {}
draws = {}
defeats = {}
points = {}

lst = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]

for i in lst:
    if i[0] in numGames:
        numGames[i[0]] += 1
    else:
        numGames[i[0]] = 1
    if i[2] in numGames:
        numGames[i[2]] += 1
    else:
        numGames[i[2]] = 1

    if i[1] > i[3]:
        if i[0] in wins:
            wins[i[0]] += 1
        else:
            wins[i[0]] = 1
        if i[2] in defeats:
            defeats[i[2]] += 1
        else:
            defeats[i[2]] = 1
        if i[0] in points:
            points[i[0]] += 3
        else:
            points[i[0]] = 3
    elif i[1] == i[3]:
        if i[0] in draws:
            draws[i[0]] += 1
        else:
            draws[i[0]] = 1
        if i[2] in draws:
            draws[i[2]] += 1
        else:
            draws[i[2]] = 1
        if i[0] in points:
            points[i[0]] += 1
        else:
            points[i[0]] = 1
        if i[2] in points:
            points[i[2]] += 1
        else:
            points[i[2]] = 1
    elif i[1] < i[3]:
        if i[2] in wins:
            wins[i[2]] += 1
        else:
            wins[i[2]] = 1
        if i[0] in defeats:
            defeats[i[0]] += 1
        else:
            defeats[i[0]] = 1
        if i[2] in points:
            points[i[2]] += 3
        else:
            points[i[2]] = 3


print(numGames)
print(wins)
print(draws)
print(defeats)
print(points)"""


# 3.7 Задачи по материалам недели 0 из 5 шагов пройдено. Correct answer
"""
# 1. Создаём необходимые словари и списки 
numGames = {}
wins = {}
draws = {}
defeats = {}
points = {}
teamlst = []
lst = []

# 2. Настаиваем правильный приём инпута
n = int(input())
for i in range(n):
    lst += [input().split(';')]

# 3. Добавляем во все словари нули, чтобы после сразу включить счётчик, а не работать и ифами
for i in lst:
    numGames[i[0]], numGames[i[2]] = 0, 0
    wins[i[0]], wins[i[2]] = 0, 0
    draws[i[0]], draws[i[2]] = 0, 0
    defeats[i[0]], defeats[i[2]] = 0, 0
    points[i[0]], points[i[2]] = 0, 0

# 4. Получаем отдельный список уникальных команд, чтобы в дальнейшем использовать их как ключи к словарям 
for i in range(len(lst)):
    teamlst.append(lst[i][0])
    teamlst.append(lst[i][2])

# 5. Запускам счётчики на все запрашиваемые колонки    
for i in lst:
    numGames[i[0]] += 1
    numGames[i[2]] += 1

    if int(i[1]) > int(i[3]):
        wins[i[0]] += 1
        defeats[i[2]] += 1
        points[i[0]] += 3
    elif int(i[1]) == int(i[3]):
        draws[i[0]] += 1
        draws[i[2]] += 1
        points[i[0]] += 1
        points[i[2]] += 1
    elif int(i[1]) < int(i[3]):
        wins[i[2]] += 1
        defeats[i[0]] += 1
        points[i[2]] += 3

# 6. Выводим результат        
for i in set(teamlst):
    print(i, ':', numGames[i], ' ', wins[i], ' ', draws[i], ' ', defeats[i], ' ', points[i], sep='')"""





















# 3.7 Задачи по материалам недели 1 из 5 шагов пройден
# В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики:
# они говорили каким-то странным набором звуков.
#
# В какой-то момент один из биологов раскрыл секрет информатиков:
# они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного
# сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
#
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины,
# на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
# после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку
# #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
#
# *d*%*d*#*d*
# dacabac
#
# Sample Input 1:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Sample Output 1:
# *d*%*d*#*d*
# dacabac
#
# Sample Input 2:
# dcba
# badc
# dcba
# badc
#
# Sample Output 2:
# badc
# dcba

# 3.7 Задачи по материалам недели 1 из 5 шагов пройден. Correct answer
"""
a = 'abcd'
c = '*d%#'
docript = 'abacabadaba'
dodecript = '#*%*d*%'

alphabet = []
cipher = []

for i in a:
    alphabet.append(i)
for i in c:
    cipher.append(i)
cript = dict(zip(alphabet, cipher))
decript = dict(zip(cipher, alphabet))

for i in docript:
    print(cript[i], end='')
print()
for i in dodecript:
    print(decript[i], end='')
"""
# print()
# print(alphabet)
# print(*alphabet, sep='')
# print(cipher)
# print(cript)
# print(cript['a'])
# print(decript)