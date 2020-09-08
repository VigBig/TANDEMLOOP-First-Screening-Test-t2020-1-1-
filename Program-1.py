a = float(input("Enter 1st number :"))
type_of_operation = input("Enter type of operation :")
b = float(input("Enter 2nd number :"))

print("\nResult = ")
if type_of_operation == "+":
    print(a+b)
elif type_of_operation == "-":
    print(a-b)
elif type_of_operation == "*":
    print(a*b)
elif type_of_operation == "/":
    print(a/b)
else:
    print("Invalid operator")