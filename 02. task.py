pocket_money = float(input())
daily_sales = float(input())
costs = float(input())
gift_price = float(input())

left_money = ((5 * pocket_money) + (5 * daily_sales )) - costs

if left_money >= gift_price:
    print(f"Profit: {left_money:.2f} BGN, the gift has been purchased.")
else:
    insufficient_money = gift_price - left_money
    print(f"Insufficient money: {insufficient_money:.2f} BGN.")