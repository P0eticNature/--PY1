def get_count_char(main_str):
    main_str = main_str.lower()
    letter_dict = {}
    letter_count = 0
    for letter in main_str:
        if letter.isalpha():
            letter_dict[letter] = letter_dict.get(letter, letter_count) + 1
    return letter_dict

    # TODO посчитать количество каждой буквы в строке в аргументе str_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

dict_ = get_count_char(main_str)

def percentage():
    total_text = len(main_str)
    dict_ = get_count_char(main_str)
    for i in dict_:
        if i.isalpha():
            a = round(dict_[i] / total_text * 100, 2)
            dict_[i] = a
    return dict_

print(percentage())
