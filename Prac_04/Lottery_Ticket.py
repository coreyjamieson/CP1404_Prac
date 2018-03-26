
import random

no_of_quick_pick = int(input("How many quick picks? "))

MIN = 1
MAX = 45
number = 0
quick_pick_counter = 1
ticket =[random.randint(MIN, MAX)]
final_quick_pick = []

while quick_pick_counter <= no_of_quick_pick:
    while number <= 6:
        ticket.append(random.randint(MIN, MAX))
        if ticket[number + 1] == ticket [number]:
            print('deletion')
            del ticket[number + 1]
        else:
            number += 1
    final_quick_pick.append(ticket)
    quick_pick_counter += 1
    ticket = [random.randint(MIN, MAX)]
print(final_quick_pick)