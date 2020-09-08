num = [1,2,3,4,5,6,7,8,9]

ip = []
i = 0
my_num = "0"

while my_num != "":
        my_num = input("Enter number:")
        ip.append(my_num)

ip.remove('')
for k in range(0,len(ip)):
    ip[k] = int(ip[k])

print(ip)

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0


for i in ip:
    if(i % num[0] == 0):
        one = one+1
    if(i % num[1] == 0):
        two = two + 1
    if(i % num[2] == 0):
        three = three + 1
    if(i % num[3] == 0):
        four = four + 1
    if(i % num[4] == 0):
        five = five + 1
    if(i % num[5] == 0):
        six = six + 1
    if(i % num[6] == 0):
        seven = seven + 1
    if(i % num[7] == 0):
        eight = eight + 1
    if(i % num[8] == 0):
        nine = nine + 1

output = {
    num[0] : one,
    num[1] : two,
    num[2] : three,
    num[3] : four,
    num[4] : five,
    num[5] : six,
    num[6] : seven,
    num[7] : eight,
    num[8] : nine,
}

print(output)

