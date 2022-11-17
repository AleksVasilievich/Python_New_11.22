import interface as fase
import view as v

def button():
    if v.start() == '1':
        fase.exp()
    elif v.start() == '2':
        fase.imp()