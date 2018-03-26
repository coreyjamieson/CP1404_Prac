
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']

user_input_name = input("Please enter your username:")

if user_input_name in usernames:
    print("Access granted")
else:
    print("Access denied!")