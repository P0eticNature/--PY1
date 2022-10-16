money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
total_money = 15000
month = 0  # количество месяцев, которое можно прожить

while total_money >= 0:
    spend *= 1.05
    total_money -= spend
    month += 1

# TODO Оформить решение

print(month)
