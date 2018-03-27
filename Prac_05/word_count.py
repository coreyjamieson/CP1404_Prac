
string = input("Text :").lower()

string_list = string.split(" ")
dictionary = {}
dictionary_count = 0

for key in string_list:
    dictionary[dictionary_count] = key
    dictionary_count += 1

print(dictionary)

for i in dictionary:
    counter = 0
    for j in dictionary:
        if dictionary[i] == dictionary[j]:
            counter += 1
    print("{:>15} : {:<3}".format(dictionary[i], counter))