
import random 
#title of password generator
print("welcome to automatic  random password genateror")
#password characters
auto_char=("zxcvbnmlkjhgfdsaqwertyuiop1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%&*")
#input values
no_of_passwords=int(input('number of automatic random passwords: '))# no of passwords wanted
len_of_passwords=int(input('lenth of automatic random passwords: '))#lenth of password

print("automatic random passwords:")
#loop for the genarate password
for x in range(no_of_passwords):
    password=' '
    for y in range(len_of_passwords):
        password=password+random.choice(auto_char)
    print(password)
