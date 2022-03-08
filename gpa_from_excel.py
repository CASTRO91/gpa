from tkinter.filedialog import askopenfilenames
import openpyxl as xl


def ggpa(a):
    b = ',. '
    num_all = 0
    num_only = 0
    sum = 0
    gpa = 0
    for i in a:
        num_all += 1
        if i in b:
            continue
        elif int(i) == 1 and len(a) == num_all:
            sum += int(i)
            num_only += 1
        elif int(i) == 1 and int(a[num_all]) == 0:
            sum += 10
            num_only += 1
        elif int(i) != 0:
            sum += int(i)
            num_only += 1
        gpa = sum / num_only
    return gpa


general = 1
excel_files = askopenfilenames(title="Выберите файлы")
for afile in excel_files:
    print(afile)
    zzz = xl.load_workbook(afile)
    sheet = zzz.active
    dict_1 = []  # предметы
    arr_1 = []  # предметы
    dict_2 = []  # фамилии
    arr_2 = []  # фамилии

    ## вывод содержимого таблицы
    # for row in sheet.rows:
    #     string = ''
    #     for cell in row:
    #         string = string + str(cell.value) + ' '
    #     print(string)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    counter_round = 0  # счетчик для количества строк в таблице
    counter_round2 = 0  # счетчик для количества столбцов в таблице

    for cell in list(sheet.rows)[0]:
        if counter_round == 19:
            break
        else:
            arr_1.append(cell.value)
            dict_1 = dict(list(enumerate(arr_1)))
            counter_round += 1

    # print(arr_1)
    # print(dict_1)

    # заполнение словаря фамилиями первая фамилия начинается с ЕДИНИЦЫ
    for cell1 in list(sheet.columns)[0]:
        if counter_round2 == 22:
            break
        else:
            arr_2.append(cell1.value)
            dict_2 = dict(list(enumerate(arr_2)))
            counter_round2 += 1

    # print(arr_2)
    # print(dict_2)

    sredni = 0
    sredni_sum = 0  # сумма всех средних балов одного человека
    sredni_all = 0  # средний балл по предметам
    counter = 0  # счетчик количества строк на которые делить

    for stolb in range(2, counter_round2 - 1):
        for stroka in range(1, counter_round - 1):
            e = str(alphabet[stroka] + str(stolb))
            if sheet[e].value is not None:
                sredni = ggpa(str(sheet[e].value))
                sheet[alphabet[stroka] + str(stolb + 23)] = sredni
                sredni_sum += sredni
                counter += 1
                # print(dict_2[stolb - 1])
                # print(dict_1[stroka], sredni)
        try:
            sredni_all = sredni_sum / counter
        except ZeroDivisionError:
            break

        sheet['T' + str(stolb)] = sredni_all
        zzz.save(afile)
        zzz.close()
        # print(dict_2[stolb - 1], ':', sredni_all)
        sredni_all = 0
        counter = 0
        sredni_sum = 0
    general += 1
