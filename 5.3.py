# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('test_2.txt') as file:
    file_lines = file.readlines()

employees = {}
sum_salary = 0
for line in file_lines:
    emp_info = line.split()
    employees.update({emp_info[0]: float(emp_info[1])})
    sum_salary += float(emp_info[1])
average_sal = sum_salary / len(employees)
print(f'Average = {average_sal}')

for k, v in employees.items():
    if v < 20000:
        print(f'{k}: {v}')

