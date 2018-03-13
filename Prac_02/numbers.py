
file_in = open('numbers.txt', 'r')

number_1 = int(file_in.readline())
number_2 = int(file_in.readline())
print(number_1 + number_2)
file_in.close()