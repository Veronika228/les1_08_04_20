
revenue = int(input("Введите значение выручки.\n"))
costs = int(input("Введите значение издержек фирмы.\n"))

profitability = int(revenue) - int(costs)

if revenue < costs:
    print("Убыток")

elif revenue > costs:
    print("Прибыль")
    print("Рентабельность выручки:", profitability)

members = int(input("Введите численность сотрудников фирмы.\n"))

profitability2 = (int(revenue) - int(costs)) // members

print("Прибыль фирмы в расчете на одного сотрудника:", profitability2)
