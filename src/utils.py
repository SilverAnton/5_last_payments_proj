import json
import os


def load_foo(filename):
    """Функция загружает список банковских операций в формате <.json> и возвращает его списком словарей <.py>"""

    with open(file=os.path.abspath(filename), mode='r', encoding='utf-8') as file:
        return json.load(file)


def sort_by_date(operations):
    """Функция сортирует список словарей с банковскими операциями по дате и возвращет его"""
    work_operations = []
    for operation in operations:
        if 'date' in operation:
            work_operations.append(operation)
    return sorted(work_operations, key=lambda x: x['date'], reverse=True)


def sort_by_execute(operations):
    """Функция сортирует список словарей с банковскими операциями по выполнению операций(EXECUTED) и возвращает его"""
    work_operations = []
    for operation in operations:
        if operation['state'] == 'EXECUTED':
            work_operations.append(operation)
    return work_operations


def get_last_payment(operations):
    """Функция возвращает 5 операций из списка"""
    return operations[:5]


def show_date(date):
    """Функция принимает дату проведения операции и возвращает ее в формате дд.мм.гг"""
    work_date = date.split('T')[0].split('-')
    return f"{work_date[2]}.{work_date[1]}.{work_date[0]}"


def hide_from(from_operation):
    """Функция частично маскирует номер счета отправителя и возвращает его"""
    payer = from_operation.split(' ')[-1]
    return f"{payer[:4]} {payer[4:6]}** **** {payer[-5:-1]}"


def hide_to(to_operations):
    """Функция частично маскирует номер счета получателя и возвращает его"""
    recipient = to_operations.split(' ')[-1]
    return f"**{recipient[-5:-1]}"


def show_result():
    """Функция вызывает все, написанные ранее функции, выводит в заданном формате сведения о 5ти последних успешных
    банковских операциях"""
    load_file = load_foo('operations.json')
    sort_date = sort_by_date(load_file)
    sort_execute = sort_by_execute(sort_date)
    last_5_payments = get_last_payment(sort_execute)

    for payment in last_5_payments:
        date = show_date(payment['date'])
        print(date, payment['description'])

        try:
            payer = hide_from(payment['from'])
            print(f"{payment['from'].split(' ')[0]} {payer} -> {payment['to'].split(' ')[0]} {hide_to(payment['to'])}")
        except KeyError:
            print(payment['to'].split(' ')[0], hide_to(payment['to']))

        print(payment['operationAmount']['amount'], payment['operationAmount']['currency']['name'])
        print()


show_result()
