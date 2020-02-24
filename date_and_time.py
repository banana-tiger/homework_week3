"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    month_ago = today - timedelta(days=30)
    print(f"Сегодня - {today.strftime('%d-%m-%Y')}, вчера - {yesterday.strftime('%d-%m-%Y')}, "
          f"месяц назад - {month_ago.strftime('%d-%m-%Y')}")
    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    string_to_date = datetime.strptime(string, "%d/%m/%y %H:%M:%S.%f")
    return string_to_date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
