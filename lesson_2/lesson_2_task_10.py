def bank(money, years):
    for years in range(years):
        money += (money * 0.1)
    return money

money = float(input("Сколько денег вкладываем? "))

years = int(input("На сколько лет? "))

print(bank(money,years))