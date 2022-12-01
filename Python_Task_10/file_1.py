


def line(st):
    result_1 = []
    simbol = []
    for j in st:
        if j.isdigit():
            simbol.append(j)
        elif (not j.isdigit()) and simbol:
            result_1.append(int(''.join(simbol)))
            result_1.append(j)
            simbol = []
        elif (not j.isdigit()) and (not simbol):
            result_1.append(j)
    if simbol:
        result_1.append(int(''.join(simbol)))    
    return result_1


def calaulate(data):
    result = 0
    if len(data) == 1:
        return data[0]
    for s in data:
        if s == '*' or s == '/':
            if s == '*':
                index = data.index(s)
                result = mult(data[index - 1], data[index + 1])
                data = data[:index - 1] + [result] + data[index +2]
            else:
                index = data.index(s)
                result = div(data[index - 1], data[index + 1])
                data = data[:index - 1] + [result] + data[index +2]

    for s in data:
        if s == '+' or s == '-':
            if s == '+':
                index = data.index(s)
                result = mult(data[index - 1], data[index + 1])
                data = data[:index - 1] + [result] + data[index +2]
            else:
                index = data.index(s)
                result = div(data[index - 1], data[index + 1])
                data = data[:index - 1] + [result] + data[index +2]
    return result

def hooks(lst):
    flage = 1
    while flage == 1:
        if ')' in lst:
            for i in range(lst.index(')'), -1, -1):
                if lst[i] == '(':
                    ind = lst.index(')')
                    elem = calaulate(lst[i + 1:ind])
                    lst = lst[:i] + [elem] + lst[ind + 1:]
        elif ')' not in lst:
            flage = 0
    return calaulate(data)

st = '(1+3)*4-3'

line(st)
calaulate(line(st))
hooks(lst)




# def calaulate(data):
#     result = 0
#     while len(data) != 1:

#         while '*' in data:
#             index = data.index('*')
#             result = data[index - 1] * data[index + 1]
#             data = data[:index - 1] + [result] + data[index + 2:]
#             # data.insert(index - 1, result)  => вместо [result]


#         while '/' in data:
#             index = data.index('/')
#             result = data[index - 1] / data[index + 1]
#             data = data[:index - 1] + [result] + data[index + 2:]

#         while '+' in data:
#             index = data.index('+')
#             result = data[index - 1] + data[index + 1]
#             data = data[:index - 1] + [result] + data[index + 2:]

#         while '-' in data:
#             index = data.index('-')
#             result = data[index - 1] - data[index + 1]
#             data = data[:index - 1] + [result] + data[index + 2:]
#     return result

# stroka = '-21+3*2+8/2-7'
# print(line(stroka))

# res = line(stroka)
# print(calaulate(res))


# def line(st):
#     result_1 = []
#     simbol = ''
#     for j in st:
#         if j.isdigit():
#             simbol += j
#         else:
#             result_1.append(float(simbol))
#             result_1.append(j)
#             simbol = ''
#     result_1.append(float(simbol))    
#     return result_1

# st = '1-30*4-3'
# print(line(st))
