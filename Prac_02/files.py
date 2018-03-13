
out_file = open('name_file.txt','w')

user_name = input('Please enter your name:')
print(user_name, file=out_file)

out_file.close()