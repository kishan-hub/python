t=eval(input("Enter some tuple of numbers:"))
l=len(t)
sum=0
for x in t:
    sum=sum+x
print("The Sum:",sum)
print("The Average:",int(sum/l))