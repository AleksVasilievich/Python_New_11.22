import view as v

# def mod_1():
#     ls = v.ponebook().split(',')
#     return ','.join(ls)
# # print(mod_1())
def mod_1():
    # ls = v.ponebook().split(',')
    return ','.join(v.ponebook().split(','))
# print(mod_1())


def mod_2():
    return '\n\n'.join(v.ponebook().split(','))
# print(mod_2())