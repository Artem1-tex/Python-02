price = input("Введіть ціну:")
discount = input("Введіть знижку:")
price_1 = int(price)
discount_1 = int(discount)

main_price = (price_1 * discount_1) // 100
result = price_1 - main_price
print(result)