#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран числа по определенному правилу
#Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
#Регулярные выражения использовать нельзя
#Натуральные числа. Выводит на экран только простые числа. Минимальное и максимальное число выводятся прописью.
primal = {'2': 'два', '3': 'три',  '5': 'пять',  '7': 'семь'}

work_buffer = ''
with open('data.txt') as input_file:
    s = ""
    buffer = input_file.read(1)
    while buffer:
        work_buffer = ''
        while buffer != ' ' and buffer != ',' and buffer != '!' and buffer != '?':
            work_buffer += buffer
            buffer = input_file.read(1)
            work_buffer += buffer
            s += buffer
            if not buffer:
                break
            buffer.replace(" ", "")
            buffer.replace("\n", "")
        buffer = input_file.read(1)
blocks = s.split(" ")
print(blocks)
print('\n')

max_min_array = []
temp_row = ""
primal_row = ""
for i in range(0, blocks.__len__()):
    for j in range(0, blocks[i].__len__()):
        temp_row += blocks[i][j]
        if (blocks[i][j] == '2' or blocks[i][j] == '3' or blocks[i][j] == '5' or blocks[i][j] == '7'):
            primal_row += blocks[i][j]
        for q in range(0, primal_row.__len__()):

            if (primal_row[q] == '2' or primal_row[q] == '3' or primal_row[q] == '5' or primal_row[q] == '7'):
             max_min_array.append(int(primal_row[q]))
    if max_min_array:
        print("блок: " + temp_row + " простые числа → " + primal_row + "\nминимальное число: " + primal[min(primal_row)] + "\nмаксимальное число: " + primal[max(primal_row)])     
        print('\n')
    max_min_array.clear()
    temp_row=''
    primal_row=''
