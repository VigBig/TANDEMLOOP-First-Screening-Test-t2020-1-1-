a = int(input("Enter an integer:"))

i=1

if a%2 != 0:
    while i <= (a*2):
        if i%2 != 0:
            print(i)
        i=i+1

else:
    while i <= ((a-1)*2):
        if i%2 != 0:
            print(i)
        i=i+1

