salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
month = 9
need_money = need_money + spend - salary

while month != 0:
    spend *= 1.03
    need_money = need_money + spend - salary
    month -= 1
# TODO Оформить решение

print(round(need_money))
