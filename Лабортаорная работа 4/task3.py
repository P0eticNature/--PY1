def delete(list_, index=None):
    left_part = list_[:index+1]
    right_part = list_[index+2:]
    list_ = left_part + right_part
    return list_

     # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4], index=4))
