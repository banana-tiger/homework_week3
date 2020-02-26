"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import random
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('names.csv', 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        names = [element[0] for element in reader]

    jobs = ['carpenter', 'waiter', 'doctor', 'teacher', 'policeman', 'programmer', 'rapper']

    list_of_dicts = [{'name': random.choice(names), 'age': random.randrange(18, 60), 'job': random.choice(jobs)}  for i in range(0, 100)]
    with open('csv_to_dict_result.csv', 'w', encoding='utf-8', newline='') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=",")
        writer.writeheader()
        for human in list_of_dicts:
            writer.writerow(human)


if __name__ == "__main__":
    main()
