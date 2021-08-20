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
                # d.split(',')[5].strip(),
                # d.split(',')[6].strip(),
            ]
            for d in data]
    return data

# Читаем файл с решениями от участников и берём оттуда степик и их решение
def read_csv_informatics_output(file_path):
    csv.field_size_limit(100000000)
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

def comparising(val, answer):
    data = ([
        ['stepic_id'] +  # stepic id
        ['name'] +
        ['number_of_task'] +
        ['score'] +
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

    task_1 = 1
    task_1_for_row_val = 2
    task_1_informatics_step_id = '1935834'

    task_2 = 2
    task_2_for_row_val = 3
    task_2_informatics_step_id = '1935836'

    task_3 = 3
    task_3_for_row_val = 4
    task_3_informatics_step_id = '1935835'

    task_4 = 4
    task_4_for_row_val = 5
    task_4_informatics_step_id = '1949636'

    task_5 = 5
    task_5_for_row_val = 6
    task_5_informatics_step_id = '1949634'

    for row_val in val:
        if float(row_val[task_1_for_row_val]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[
                    4] == task_1_informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            [task_1] +  # number_of_task
                            [float(row_val[task_1_for_row_val])] +  # score
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)

        if float(row_val[task_2_for_row_val]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[
                    4] == task_2_informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            [task_2] +  # number_of_task
                            [float(row_val[task_2_for_row_val])] +  # score
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)

        if float(row_val[task_3_for_row_val]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[
                    4] == task_3_informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            [task_3] +  # number_of_task
                            [float(row_val[task_3_for_row_val])] +  # score
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)

        # if float(row_val[task_4_for_row_val]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[
                    4] == task_4_informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            [task_4] +  # number_of_task
                            [float(row_val[task_4_for_row_val])] +  # score
                            [row_answer[1]] +  # hint
                            [row_answer[2]] +  # status
                            [row_answer[3]] +  # reply
                            [row_answer[4]] +  # step id
                            [passed_test] +
                            [max_tests]
                        ])
                        max_result_before = max(max_tests)

        # if float(row_val[task_5_for_row_val]) != 0:
            max_tests = []
            max_result_before = 0
            for row_answer in answer:
                if row_val[0] == row_answer[0] and row_answer[2] == 'correct' and row_answer[
                    4] == task_5_informatics_step_id:
                    if row_answer[1][row_answer[1].find('test(s) passed') - 9] == 'n':
                        passed_test = int(row_answer[1][row_answer[1].find('test(s) passed') - 8])
                        max_tests.append(int(row_answer[1][row_answer[1].find('test(s) passed') - 8]))
                    else:
                        passed_test = int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7])
                        max_tests.append(int(
                            row_answer[1][
                            row_answer[1].find('test(s) passed') - 9:row_answer[1].find('test(s) passed') - 7]))
                    while max(max_tests) > max_result_before:
                        data += ([
                            [row_answer[0]] +  # stepic id
                            [row_val[1]] +  # name
                            [task_5] +  # number_of_task
                            [float(row_val[task_5_for_row_val])] +  # score
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




# Функция comparising возвращает нам массив,
# мы построчно проходимся по нему и возвращаем только строки с максимальным результатом
def reply_outputs(comparising_result):
    data = ([
        ['stepic_id'] +
        ['name'] +
        ['number_of_task'] +
        ['score'] +
        ['hint'] +
        ['status'] +
        ['reply'] +
        ['language'] +
        ['step_id'] +
        ['passed_test'] +
        ['max_tests']
    ])
    for row in comparising_result:
        if max(row[9]) == row[8]:
            # data += ([row])
            if 'python3' in row[6]:
                language = 'python3'
            elif 'c++' in row[6]:
                language = 'c++'
            elif 'kotlin' in row[6]:
                language = 'kotlin'
            elif 'mono c#' in row[6]:
                language = 'mono c#'
            elif 'java11' in row[6]:
                language = 'java11'
            else: language = 'unknown'
            data += ([
                [row[0]] +
                [row[1]] +
                [row[2]] +
                [row[3]] +
                [row[4]] +
                [row[5]] +
                [row[6]] +
                [language] +
                [row[8]] +
                [row[9]]
            ])

    # myFile = open('/Users/nabal/Downloads/Умный город. 28.02-05.03/! Умный город. Сборка для скрипта/Умный город. Информатика для скрипта/reply_outputs.csv', 'w')
    # with myFile:
    #     writer = csv.writer(myFile)
    #     writer.writerows(data)
    return data

def bag_trap(val_data, reply_data):
    bag_trap_data = ([
        ['stepic_id'] +
        ['name'] +
        ['number_of_task'] +
        ['score'] +
        ['hint'] +
        ['status'] +
        ['reply'] +
        ['language'] +
        ['step_id'] +
        ['passed_test'] +
        ['max_tests']
    ])

    sum_val = 0
    sum_reply = 0
    for row_val in val_data:
        sum_val += float(row_val[2])
        sum_val += float(row_val[3])
        sum_val += float(row_val[4])
        print(float(row_val[2]))
        print(float(row_val[3]))
        print(float(row_val[4]))
    print()
    for row_reply in reply_data:
        if row_reply[3] == 'score':
            continue
        sum_reply += float(row_reply[3])
        print(float(row_reply[3]))

    print(sum_val, sum_reply)
    # for row_val in val_data:
    #     for row_reply in reply_data:
    #         if row_reply[2] == '1' and float(row_reply[3]) != float(row_val[3]):
    #             bag_trap_data += ([
    #                 [row_reply[0]] +
    #                 [row_reply[1]] +
    #                 [row_reply[2]] +
    #                 [row_reply[3]] +
    #                 [row_reply[4]] +
    #                 [row_reply[5]] +
    #                 [row_reply[6]] +
    #                 [row_reply[7]] +
    #                 [row_reply[8]] +
    #                 [row_reply[9]]
    #                 # [row_reply[10]]
    #             ])
    #             print('not ok')
    #
    #         elif row_reply[2] == '2' and float(row_reply[3]) != float(row_val[4]):
    #             bag_trap_data += ([
    #                 [row_reply[0]] +
    #                 [row_reply[1]] +
    #                 [row_reply[2]] +
    #                 [row_reply[3]] +
    #                 [row_reply[4]] +
    #                 [row_reply[5]] +
    #                 [row_reply[6]] +
    #                 [row_reply[7]] +
    #                 [row_reply[8]] +
    #                 [row_reply[9]]
    #                 # [row_reply[10]]
    #             ])
    #             print('not ok')
    #         elif row_reply[2] == '3' and float(row_reply[3]) != float(row_val[5]):
    #             bag_trap_data += (
    #                 [[row_reply[0]] +
    #                 [row_reply[1]] +
    #                 [row_reply[2]] +
    #                 [row_reply[3]] +
    #                 [row_reply[4]] +
    #                 [row_reply[5]] +
    #                 [row_reply[6]] +
    #                 [row_reply[7]] +
    #                 [row_reply[8]] +
    #                 [row_reply[9]]
    #                 # [row_reply[10]]
    #             ])
    #             print('not ok')
    # print(bag_trap_data)


# val = read_csv_informatics('/Users/nabal/Downloads/Искусственный интеллект. Итоговый Протокол (финальные баллы участников) - Протокол по предмету 1 (копия)-3.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/lesson-495130-submissions-full.csv')
# comparising_result = comparising(val, answer)
# informatics_step_id = ['2032313', '2032311', '2032312', '2032315', '2032314']

# Умный город
val = read_csv_informatics('/Users/nabal/Downloads/Умный город. 28.02-05.03/! Умный город. Сборка для скрипта/Умный город. Информатика для скрипта/Умный город. Протокол (итоговый, командной работы, предметный, апелляция, состав предметных жюри, состав методической комиссии и жюри) - Протокол по предмету 1 (для скрипта).csv')
answer = read_csv_informatics_output('/Users/nabal/Downloads/Умный город. 28.02-05.03/! Умный город. Сборка для скрипта/Умный город. Информатика для скрипта/lesson-488582-submissions-full.csv')
comparising_result = comparising(val, answer)
informatics_step_id = ['2032313', '2032311', '2032312', '2032315', '2032314']



# print(reply_outputs(comparising_result))
print(bag_trap(val, comparising_result))

# Фио
# Номер задачи
# Кол-во баллов
# Код
