"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', "r", encoding="utf-8") as file:
        referat = ''
        for line in file:
            referat += line
    referat_len = len(referat)
    trash_list = ['.', ',', '!', '?']
    words_count = 0
    for word in referat.split():
        if word in trash_list:
            continue
        else:
            words_count += 1
    referat2 = referat.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as file:
        file.write(f'Результаты: длина файла = {referat_len},  количество слов = {words_count}. Измененный текст: '
                   f'{referat2}')

if __name__ == "__main__":
    main()
