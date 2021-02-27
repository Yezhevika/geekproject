prices = [10.3, 12.5, 34.8, 45, 57.8, 46.51, 97, 34.7, 90, 57.9]

kop = 0
rub = 0
for i in prices:
    money = str(i).split('.')
    if len(money) == 2:
        rub, kop = money
    print(f"{rub} руб {int(kop):02d} коп,", end=" ")

print(f'ID base: {id(prices)} - {prices}')
prices.sort()
print(f'ID base: {id(prices)} - {prices}')

print(f'ID change: {id(sorted(prices))} - {sorted(prices, reverse = True)}\n{sorted(prices,reverse = True)}[:6]')