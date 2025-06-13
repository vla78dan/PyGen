num = int(input())
q  = num % 10
w =  (num % 100) // 10
e = num // 100
sum_num = q + e + w
product_of_numbers = q * w * e

print('Сумма цифр =', sum_num)
print('Произведение цифр =', product_of_numbers)