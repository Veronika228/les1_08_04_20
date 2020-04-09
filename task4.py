
number = int(input("Введите целое положительное число.\n"))

a_number: int = number % 10
b_number: int = (number // 10) % 10
c_number: int = number // 100

if number < 10:
    print(number)

while number >= 10:
    if a_number > b_number and a_number > c_number:
        print(a_number)
        break
    if b_number > c_number and b_number > a_number:
        print(b_number)
        break
    if c_number > a_number and c_number > b_number:
        print(c_number)
        break
