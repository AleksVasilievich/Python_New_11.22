import logger as log
import view as v

def exp():
    with open('Python_seminar_7/data_1.txt', 'a', encoding='utf_8') as file:
        file.write(log.mod_1())

    with open('Python_seminar_7/data_2.txt', 'a', encoding='utf_8') as file:
        file.write(log.mod_2())

def imp():
    path = 'Python_seminar_7/data_1.txt'
    data = open(path, 'r', encoding='utf_8')
    for line in data:
        print(line)
    data.close()

    path = 'Python_seminar_7/data_2.txt'
    data = open(path, 'r', encoding='utf_8')
    for line in data:
        print(line, end='')
    data.close()