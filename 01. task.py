number_of_people = int(input())
number_of_nights = int(input())
number_cards = int(input())
number_tickets = int(input())

sum = ((number_of_nights * 20) + (number_cards * 1.60) + (number_tickets * 6))* number_of_people * 1.25

print(format(sum,".2f"))