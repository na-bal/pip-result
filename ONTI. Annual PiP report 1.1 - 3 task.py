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

def comparising(val, answer, informatics_step_id):
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
    task_1_informatics_step_id = informatics_step_id[0]

    task_2 = 2
    task_2_for_row_val = 3
    task_2_informatics_step_id = informatics_step_id[1]

    task_3 = 3
    task_3_for_row_val = 4
    task_3_informatics_step_id = informatics_step_id[2]

    task_4 = 4
    task_4_for_row_val = 5
    task_4_informatics_step_id = informatics_step_id[3]

    task_5 = 5
    task_5_for_row_val = 6
    task_5_informatics_step_id = informatics_step_id[4]

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
def reply_outputs(comparising_result, result_output):
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
                language = 'python'
            elif 'c++' in row[6]:
                language = 'cpp'
            elif 'kotlin' in row[6]:
                language = 'kotlin'
            elif 'mono c#' in row[6]:
                language = 'csharp'
            elif 'java11' in row[6]:
                language = 'java'
            elif 'pascalabc' in row[6]:
                language = 'pascal'
            elif 'ruby' in row[6]:
                language = 'Ruby'
            elif 'rust' in row[6]:
                language = 'Rust'
            elif 'scala' in row[6]:
                language = 'Scala'
            elif 'c' in row[6]:
                language = 'cpp'

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
                [row[7]] +
                [row[9]] +
                [row[8]]
            ])

    myFile = open(result_output, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)
    return data

def bug_report(val, reply_outputs, bug_output):
    data = ([
        ['cnt_val'] +
        ['cnt_reply'] +
        ['bug type'] +
        ['row_val']
    ])

    cnt_val = 0
    for row_val in val:
        if float(row_val[2]) != 0:
            cnt_val += 1
        if float(row_val[3]) != 0:
            cnt_val += 1
        if float(row_val[4]) != 0:
            cnt_val += 1
        # if float(row_val[5]) != 0:
            cnt_val += 1
        # if float(row_val[6]) != 0:
            cnt_val += 1
    print('кол-во правильно решённых задач в исходном документе:', cnt_val)

    cnt_reply = len(reply_outputs) - 1
    print('кол-во правильно решённых задач в итоговый выгрузке:', cnt_reply)

    # проверка по степикам
    stepic_lst = []
    # name_lst = []
    if cnt_val != cnt_reply:
        print('BUG!')
        for row_reply in reply_outputs:
            stepic_lst.append(row_reply[0])
            # name_lst.append(row_reply[1])

        for row_val in val:
            if row_val[0] not in stepic_lst and (row_val[2] != '0' or row_val[3] != '0' or row_val[4] != '0'):
                print(row_val)
                data += ([
                    [cnt_val] +
                    [cnt_reply] +
                    ['отсутствует степик'] +
                    [row_val]
                ])

    # name_lst = []
    # if cnt_val != cnt_reply:
    #     for row_val in val:
    #         if row_val[1] not in name_lst and (row_val[2] != '0' or row_val[3] != '0' or row_val[4] != '0' or row_val[5] != '0' or row_val[6] != '0'):


    myFile = open(bug_output, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)




# template
# informatics_step_id = ['1974489', '1974493', '1974491', '1974492', '1974494']
# val = read_csv_informatics()
# answer = read_csv_informatics_output()
# result_output =
# bug_output =
# comparising_result = comparising(val, answer, informatics_step_id)


# # Автоматизация бизнес-процессов
# informatics_step_id = ['1974489', '1974493', '1974491', '1974492', '1974494']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автоматизация бизнес-процессов. Итоговый протокол  (Копия для ЭС 2) - Протокол по предмету 1 (для скрипта) -- 5 задач.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автоматизация бизнес-процессов. Решения.csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автоматизация бизнес-процессов. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автоматизация бизнес-процессов. Bugs.csv'
# comparising_result = comparising(val, answer)


# Искуственный интеллект
# informatics_step_id = ['1949635', '1949632', '1949633', '1949636', '1949634']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Искусственный интеллект. Итоговый Протокол (финальные баллы участников) - Протокол по предмету 1 (для скрипта) -- 5 задач.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Искусственный интеллект. Решения.csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Искусственный интеллект. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Искусственный интеллект. Bugs.csv'
# comparising_result = comparising(val, answer, informatics_step_id)

# Большие даннные и Машинное обучение
# informatics_step_id = ['1949635', '1949632', '1949633', '1949636', '1949634']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Большие данные и машинное обучение. Итоговый протокол(финальные баллы участников) - Протокол по предмету 1 (для скрипта) -- 5 задач.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Большие данные и машинное обучение. Решения.csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Большие данные и машинное обучение. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Большие данные и машинное обучение. Bugs.csv'
# comparising_result = comparising(val, answer, informatics_step_id)

# Беспилотные авиационные системы
# informatics_step_id = ['1846037', '1846038', '1846039', '1846040', '1846041']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Беспилотные авиационные системы. Итоговый протокол (финальные баллы участников) - Протокол по предмету 1 (для скрипта) -- 5 задач.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Беспилотные авиационные системы. Решения.csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Беспилотные авиационные системы. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Беспилотные авиационные системы. Bugs.csv'
# comparising_result = comparising(val, answer, informatics_step_id)


# Летающая робототехника
# informatics_step_id = ['1846037', '1846038', '1846039', '1846040', '1846041']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Летающая робототехника. Итоговый протокол (финальные баллы участников) - Протокол по предмету 1 (для скрипта) -- 5 задач.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Летающая робототехника. Решения (исправлено вручную).csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Летающая робототехника. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Летающая робототехника. Bugs.csv'
# comparising_result = comparising(val, answer, informatics_step_id)


# Нейротехнологии и когнитивные науки
# informatics_step_id = ['1949635', '1949632', '1949633', '1949636', '1949634']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Нейротехнологии и когнитивные науки. Шаблон итогового протокола (финальные баллы участников) - Протокол по предмету 1 (для скрипта) -- 5 задач.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Нейротехнологии и когнитивные науки. Решения.csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Нейротехнологии и когнитивные науки. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Нейротехнологии и когнитивные науки. Bugs.csv'
# comparising_result = comparising(val, answer, informatics_step_id)


# Ядерные технологии
# informatics_step_id = ['2032313', '2032311', '2032312', '2032315', '2032314']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Ядерные технологии. Итоговый протокол (финальные баллы участников) - Протокол по предмету 1 (для скрипта) -- 5 задач.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Ядерные технологии. Решения.csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Ядерные технологии. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Ядерные технологии. Bugs.csv'
# comparising_result = comparising(val, answer, informatics_step_id)

# Автономные транспортные системы
# informatics_step_id = ['1935834', '1935836', '1935835', '00000000', '00000000']
# val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автономные транспортные системы. Протокол (итоговый, командной работы, предметный, апелляция, состав предметных жюри, состав методической комиссии и жюри) - Протокол по предмету 1 (для скрипта) -- 3 задачи.csv')
# answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автономные транспортные системы. Решения.csv')
# result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автономные транспортные системы. Итоговая сборка.csv'
# bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Автономные транспортные системы. Bugs.csv'
# comparising_result = comparising(val, answer, informatics_step_id)

# Передовые производственные технологии
informatics_step_id = ['1935834', '1935836', '1935835', '00000000', '00000000']
val = read_csv_informatics('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Передовые производственные технологии. Протокол (итоговый, командной работы, предметный, апелляция, состав предметных жюри, состав методической комиссии и жюри) - Протокол по предмету 1 (для скрипта) -- 3 задачи.csv')
answer = read_csv_informatics_output('/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Передовые производственные технологии. Решения.csv')
result_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Передовые производственные технологии. Итоговая сборка.csv'
bug_output = '/Users/nabal/Downloads/!!! СБОРКААААА - предметка/!!!!!! Информатика/Выгрузки/Передовые производственные технологии. Bugs.csv'
comparising_result = comparising(val, answer, informatics_step_id)


# print(reply_outputs(comparising_result, result_output))
print(bug_report(val, reply_outputs(comparising_result,result_output), bug_output))
# print(bag_trap(val, comparising_result))
