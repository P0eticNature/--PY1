def get_count_char(str_):
    str_ = {}
    letter_count = 0
    for letter in main_str:
        str_[letter] = str_.get(letter, letter_count) + 1
    return str_

    # TODO посчитать количество каждой буквы в строке в аргументе str_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = "".join(main_str.split())
main_str = "".join(main_str.split(","))
main_str = "".join(main_str.split("."))
main_str = "".join(main_str.split("!"))
main_str = main_str.lower()

print(get_count_char(main_str))
