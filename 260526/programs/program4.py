a = input("enter the value of the first variable (a): ")
b = input("enter the value of the second variable (b): ")
print(f"original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"swapped values: a = {a}, b = {b}")
