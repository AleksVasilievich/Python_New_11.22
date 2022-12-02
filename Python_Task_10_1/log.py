id_user = None
input_data = None
result = None

def id_user(num_id):
    global id_user
    id_user = num_id

def input_data(data):
    global input_data
    input_data = data

def results(res):
    global result
    result = res

def write_log():
    with open('Python_Task_10_1\log_data.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'ID user: {id_user}, Input: {input_data}, Result: {result}\n')



