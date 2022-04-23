import os
os.system('cls')

User_choice = input("Enter your choice \n1.Encryption\n2.Decryption :") 

if User_choice == '1':
    my_str = input("Enter a string: ")

    nums = []

    for char in my_str:
        nums.append(str(ord(char)+113))

    print(','.join(nums))
elif User_choice == '2':
    my_code = input ("Enter Encrypted sentence (cama seperated):")

    string_list = []

    for i in my_code.split(','):
        string_list.append(chr(int(i)-113))
    print(''.join(string_list))

else:
    print("Invalid Input")