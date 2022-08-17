number_sea = int(input())
number_mountain = int(input())

profit = 0

while True:
    vacation_type = input()
    if vacation_type == "sea":
        if number_sea > 0:
            profit += 680
            number_sea -= 1
    elif vacation_type == "mountain":
        if number_mountain > 0:
            profit += 499
            number_mountain -= 1
    elif vacation_type == "Stop":
        break

    if number_sea == 0 and number_mountain == 0:
        print("Good job! Everything is sold.")
        break

print(f"Profit: {profit} leva.")