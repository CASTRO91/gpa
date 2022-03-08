a = '1010919192375757482.  7654,.9'
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

print('сумма всех чисел:', sum)
print('количество чисел:', num_only)
gpa = sum / num_only
print('средний балл:', gpa)
