n1=int(input("Enter the first No"))
n2=int(input("Enter the second No"))
n3=int(input("Enter the third no"))

if n1>n2 and n1>n3:
    print("Biggest no is ",n1)
elif n2>n3:
    print("Biggest no is ",n2)
else:
    print("Biggest no is ",n3)