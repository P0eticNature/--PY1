# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint


def list_of_dict():
    mega_list = []
    num = 0
    while num != 16:
        number_dict = {'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)}
        mega_list.append(number_dict)
        num += 1
    return mega_list

pprint(list_of_dict())
