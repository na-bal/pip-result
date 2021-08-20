import csv
import sys

# Читаем файл с баллами участников. На выходе список из Степик ИД, ФИО, и баллов
def read_csv_informatics(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.splitlines()[1:]
        data = [
            [
                d.split(',')[0].strip(), # Степик ИД
                d.split(',')[1].strip(), # ФИО
                d.split(',')[2].strip(), # Задача 1 и далее до 5
                d.split(',')[3].strip(),
                d.split(',')[4].strip(),
                d.split(',')[5].strip(),
                d.split(',')[6].strip(),
            ]
            for d in data]
    return data

# Читаем файл с решениями от участников и берём оттуда степик и их решение
def read_csv_informatics_output(file_path):
    csv.field_size_limit(100000000)
    # csv.field_size_limit(sys.maxsize)
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_reader:
            data += ([
                [row[2]] +      # stepic
                [row[12]] +     # hint
                [row[7]] +      # status
                [row[10]] +     # reply
                [row[1]]        # step id
            ])
        return data

# Смотрим в таблицу с баллами, ищем где они есть и заглядываем в таблицу в решениями,
# достаём оттуда различные параметры, в т.ч. создаём список с пройденными тестами,
# чтобы вдальнейшем выбрать из них максимальный
def comparising_old_0_1(val, answer):
    cnt = 0 # счётчик, чтобы понимать что за строка
    for row in val:
    # print(row)
        if float(row[3]) != 0:
            print(row[0], row[1], row[3])
            for row_answer in answer:
                cnt += 1 # удалить, когда всё заработает
                if row[0] == row_answer[0]:
                    print('line', cnt) # удалить, когда всё заработает
                    print(row_answer[1])

def comparising_old_0_2(val, answer):
    cnt = 0                         # счётчик, чтобы понимать что за строка
    max_tests = []
    data = []
    passed_test = ''
    for row_val in val:
    # print(row)
        if float(row_val[3]) != 0:
            print(row_val[0], row_val[1], row_val[3])
            for row_answer in answer:
                cnt += 1            # удалить, когда всё заработает
                if \
                        row_val[0] == row_answer[0]\
                                and row_answer[2] == 'correct'\
                                and row_answer[4] in informatics_step_id:
                    print('>>> line >>>', cnt)      # удалить, когда всё заработает
                    print(row_answer)
                    print(row_answer[1])
                    print(type(row_answer[1]))
                    print('index --', row_answer[1].find('test(s) passed'))
                    print('test:', row_answer[1][row_answer[1].find('test(s) passed') - 9 : row_answer[1].find('test(s) passed')] )
                    print()
                    print('end function')
                    print()
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        max_tests.append(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        passed_test = row_answer[1][row_answer[1].find('test(s) passed') - 8]
                    else:
                        max_tests.append(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        passed_test = row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]
                    print('max tests =', max_tests)
                    data += ([
                        [row_answer[0]] +  # stepic id
                        [row_answer[1]] +  # hint
                        [row_answer[2]] +  # status
                        [row_answer[3]] +  # reply
                        [row_answer[4]] + # step id
                        [passed_test]
                    ])
                myFile = open('/Users/nabal/Downloads/test.csv', 'w')
                with myFile:
                    writer = csv.writer(myFile)
                    writer.writerows(data)
                print(data)

def comparising_old_0_3(val, answer):
    data = ([
        ['stepic_id'] +  # stepic id
        ['name'] +
        ['number_of_task'] +
        ['hint'] +  # hint
        ['status'] +  # status
        ['reply'] +  # reply
        ['step_id'] +  # step id
        ['passed_test'] +
        ['max_tests']
    ])
    passed_test = ''
    number_of_task = ''
    max_tests = []
    max_result = 0
    max_result_before = 0
    informatics_step_id = ['2032313', '2032311', '2032312', '2032315', '2032314']
    for row_val in val:
        if float(row_val[3]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[4] in informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +     # name
                            ['2'] +            # number_of_task
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] + # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)
        if float(row_val[2]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[4] in informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(row_answer[1][
                                      row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find(
                            'test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            ['1'] +  # number_of_task
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)
    # myFile = open('/Users/nabal/Downloads/test.csv', 'w')
    # with myFile:
    #     writer = csv.writer(myFile)
    #     writer.writerows(data)
    return data

def comparising(val, answer):
    data = ([
        ['stepic_id'] +  # stepic id
        ['name'] +
        ['number_of_task'] +
        ['hint'] +  # hint
        ['status'] +  # status
        ['reply'] +  # reply
        ['step_id'] +  # step id
        ['passed_test'] +
        ['max_tests']
    ])
    passed_test = ''
    number_of_task = ''
    max_tests = []
    max_result = 0
    max_result_before = 0
    informatics_step_id = ['2032313', '2032311', '2032312', '2032315', '2032314', '1949641', '1949635', '1949632', '1949633', '1949636', '1949634']
    for row_val in val:
        if float(row_val[2]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                # print('stepik', row_val[0])
                # print('stepik', row_answer[0])
                # print('status',row_answer[2])
                # print('step',row_answer[4])
                # print('...')
                # print()
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[4] in informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +     # name
                            ['1'] +            # number_of_task
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] + # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)
        if float(row_val[3]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[4] in informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(row_answer[1][
                                      row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find(
                            'test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            ['2'] +  # number_of_task
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)
        if float(row_val[4]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[4] in informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(row_answer[1][
                                      row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find(
                            'test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            ['3'] +  # number_of_task
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)
        if float(row_val[5]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[4] in informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(row_answer[1][
                                      row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find(
                            'test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            ['4'] +  # number_of_task
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)
        if float(row_val[6]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[4] in informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(row_answer[1][
                                      row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 9:row_answer[1].find(
                            'test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            ['5'] +  # number_of_task
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)
    myFile = open('/Users/nabal/Downloads/test.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)
    return data





# def read_csv_comparising_result(file_path):
#     with open(file_path) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         data = []
#         for row in csv_reader:
#             data += ([
#                 [row[0]] +
#                 [row[1]] +
#                 [row[2]] +
#                 [row[3]] +
#                 [row[4]] +
#                 [row[5]] +
#                 [row[6]] +
#                 [row[7]] +
#                 [row[8]]
#             ])
#         return data


# Функция comparising возвращает нам массив,
# мы построчно проходимся по нему и возвращаем только строки с максимальным результатом
def reply_outputs(comparising_result):
    line = 0
    for row in comparising_result:
        # print('>>> line:', line)
        # print(row)
        # print(max(row[8]) == row[7])
        # print(max(row[8]), row[7])
        # print(type(max(row[8])), type(row[7]))
        # # print('passed_test:', row[7])
        # # print(type(row[7]))
        # # print('max_tests:', row[8])
        # # print(row[8])
        # # print('max:', max(row[8]))
        # print('...')
        # line += 1

        if max(row[8]) == row[7]:
            print('> start func')
            print('name:', row[1])
            print('number_of_task:', row[2])
            print('reply:', row[5])
            print('passed_test:', row[7])
            print('max_tests:', row[8])
            print('stop func')
            print('...')
            print()




# Введи сюда пути к файлам
# val = read_csv_informatics('/Users/nabal/Downloads/Урбанистика. Итоговый протокол (финальные баллы участников) - TMP-2.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/Урбанистика. Итоговый протокол (финальные баллы участников) - TMP 2-2.csv')
# comparising_result = comparising(val, answer)
# informatics_step_id = ['2032313', '2032311', '2032312', '2032315', '2032314']

val = read_csv_informatics('/Users/nabal/Downloads/Искусственный интеллект. Итоговый Протокол (финальные баллы участников) - Протокол по предмету 1 (копия)-3.csv')
answer = read_csv_informatics_output('/Users/nabal/Downloads/lesson-495130-submissions-full.csv')
comparising_result = comparising(val, answer)
informatics_step_id = ['2032313', '2032311', '2032312', '2032315', '2032314']



print(reply_outputs(comparising_result))
