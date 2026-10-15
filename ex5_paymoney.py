amount = int(input("Введите сумму сдачи:"))

coins = [50,10,5,2,1]

for coin in coins:
    while amount >= coin:
        print("Монета:", coin)
        amount = amount - coin
        