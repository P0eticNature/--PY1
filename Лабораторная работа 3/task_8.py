money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить

total_money = money_capital + salary
spending_percent = 1 + increase

while total_money >= 0:
    spend *= spending_percent
    total_money -= spend
    month += 1

print(month)
