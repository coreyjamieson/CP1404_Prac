
numbers = []
loop_exit = 0

while loop_exit <= 4:
    numbers.append(input("Number: "))
    loop_exit += 1

print("The first number is: {}".format(numbers[0]))
print("The last number is: {}".format(numbers[4]))
print("The smallest number is: {}".format(min(numbers)))
print("The largest number is : {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

