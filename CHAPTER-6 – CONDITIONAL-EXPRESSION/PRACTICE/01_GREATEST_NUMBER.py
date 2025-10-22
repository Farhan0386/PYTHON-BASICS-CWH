a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))
d=int(input("Enter your fourth number: "))
print()
if a>b and a>c and a>d:
    print(f"The greatest number is first : {a}")
elif b>c and b>d:
    print(f"The greatest number is second : {b}")
elif c>d:
    print(f"The greatest number is third :{c}")
else:
    print(f"The gratest number is fourth : {d}")
print()
print("End of program")