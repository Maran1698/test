import random

print("welcome to automatic  random password genateror")
auto_char=("zxcvbnmlkjhgfdsaqwertyuiop1234567890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%&*")
no_of_passwords=int(input('number of automatic random passwords: '))
len_of_passwords=int(input('lenth of automatic random passwords: '))
print("automatic random passwords:")

for x in range(no_of_passwords):
    password=' '
    for y in range(len_of_passwords):
        password=password+random.choice(auto_char)
    print(password)