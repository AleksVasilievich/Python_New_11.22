


def line(st):
    result_1 = []
    simbol = ''
    for j in st:
        if j.isdigit():
            simbol += j
        else:
            result_1.append(float(simbol))
            result_1.append(j)
            simbol = ''
    result_1.append(float(simbol))    
    return result_1
    # print(result_1)


def calaulate(data):
    result = 0
    while len(data) != 1:

        while '*' in data:
            index = data.index('*')
            result = data[index - 1] * data[index + 1]
            data = data[:index - 1] + [result] + data[index + 2:]
            # data.insert(index - 1, result)  => вместо [result]


        while '/' in data:
            index = data.index('/')
            result = data[index - 1] / data[index + 1]
            data = data[:index - 1] + [result] + data[index + 2:]

        while '+' in data:
            index = data.index('+')
            result = data[index - 1] + data[index + 1]
            data = data[:index - 1] + [result] + data[index + 2:]

        while '-' in data:
            index = data.index('-')
            result = data[index - 1] - data[index + 1]
            data = data[:index - 1] + [result] + data[index + 2:]
    return result

# stroka = text
# stroka = '21+3*2+8/2-7'
# print(line(stroka))
# 
# res = line(stroka)
# print(calaulate(res))
