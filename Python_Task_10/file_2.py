
st = '1-30*4-3'
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

print(result_1)








# s = '1+3*4-3'
# if '*' in s:
#     index = s.index('*')
#     result = int(s[index - 1]) * int(s[index + 1])
#     s = s[:index - 1] + str(result) + s[index + 2:]
# print(s)
# if '+' in s:
#     index = s.index('+')
#     result = int(s[index - 1]) + int(s[index + 1])
#     s = s[:index - 1] + str(result) + s[index + 2:]
# print(s)




# # s = '1+3*4-3'

# def calc(s):
#     result = 0
#     while len(s) != 1:
#         if '*' in s:
#             index = s.index('*')
#             result = int(s[index - 1]) * int(s[index + 1])
#             s = s[:index - 1] + str(result) + s[index + 2:]

#         while '/' in s:
#             index = s.index('/')
#             result = int(s[index - 1]) / int(s[index + 1])
#             s = s[:index - 1] + str(result) + s[index + 2:]

#         while '+' in s:
#             index = s.index('+')
#             result = int(s[index - 1]) + int(s[index + 1])
#             s = s[:index - 1] + str(result) + s[index + 2:]

#         while '-' in s:
#             index = s.index('-')
#             result = int(s[index - 1]) - int(s[index + 1])
#             s = s[:index - 1] + str(result) + s[index + 2:]

#     return result        

# # s = '3*4'
# s = '1+3*4-3'
# print(calc(s))