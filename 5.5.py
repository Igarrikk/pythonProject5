# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

with open('test_num.txt', 'w') as file:
    for _ in range(30):
        file.write(f'{random.randint(0, 10)} ')

with open('test_num.txt') as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)
        print(sum)
