from src.utils import sort_by_execute, sort_by_date, show_date, show_result, get_last_payment, load_foo, hide_from, \
    hide_to

# фикстуры для удобной и корректной работы тестов
operations = load_foo('operations.json')
date_sort_operations = sort_by_date(operations)
execute_sort_operations = sort_by_execute(date_sort_operations)
last_operations = get_last_payment(execute_sort_operations)
operations_date = ['08.12.2019', '07.12.2019', '19.11.2019', '13.11.2019', '05.11.2019']
bank_accounts = ['**3590', '2842 87** **** 8901', '**5365', '7810 84** **** 8556', '**2286', '3861 14** **** 6979',
                 '**7812', '**8838']
operations_with_mark_from = [
    {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
     'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'},
    {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
     'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
    {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
     'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'},
]
finilly_result = (f"08.12.2019 Открытие вклада Счет **3590 41096.24 USD\n07.12.2019 Перевод организации Visa 2842 87** "
                  f"**** 8901 -> Счет **5365 48150.39 USD\n19.11.2019 Перевод организации Maestro 7810 84** **** 8556 "
                  f"-> Счет **2286 30153.72 руб.\n13.11.2019 Перевод со счета на счет Счет 3861 14** **** 6979 -> "
                  f"Счет **7812 62814.53 руб.\n05.11.2019 Открытие вклада Счет **8838 21344.35 руб.")


def test_load_foo():
    """тест на проверку загрузки файла формата <.json> в функцию load_foo и возврата списка <.py> """
    assert type(operations) is list


def test_sort_by_date():
    """тест проверяет сортировку по дате, функции sort_by_date"""
    assert date_sort_operations[0]['date'] > date_sort_operations[-1]['date']


def test_sort_by_execute():
    """тест проверяет сортировку списка по наличию ключа словаря <'state'> из списка словарей"""
    for operation in execute_sort_operations:
        assert operation['state'] == 'EXECUTED'


def test_get_last_payment():
    """тест проверяет возврат 5ти элементов списка"""
    assert len(last_operations) == 5


def test_show_date():
    """тест проверяет возврат даты функцией show_date в формате ДД.ММ.ГГ"""
    for one_operation in last_operations:
        result = show_date(one_operation['date'])
        assert result in operations_date


def test_hide_from_and_to():
    """тест проверяет формат маскировки номеров счета, функциями hide_from и hide_to, входящих и исходящих платежей"""
    for operation in last_operations:
        result_to = hide_to(operation['to'])
        assert result_to in bank_accounts
    for result_from in operations_with_mark_from:
        assert hide_from(result_from['from']) in bank_accounts


def test_show_result():
    """тест проверяет вывод результата функции show_result в требуемом формате задания"""
    result = show_result()
    assert result == print(finilly_result)
