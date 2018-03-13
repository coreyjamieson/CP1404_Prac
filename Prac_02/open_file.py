
file_opened = open('name_file.txt', 'r')

name = file_opened.read().strip()
print('Your name is:', name )

file_opened.close()