import random

def get_unique_list_numbers() -> list[int]:
    left_border = -10
    right_border = 11
    total_count = 15

    list_numbers = [num for num in range(left_border, right_border)]
    random.shuffle(list_numbers)

    return list_numbers[:total_count]

# TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

