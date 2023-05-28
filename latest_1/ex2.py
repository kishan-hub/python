cart=[10,20,500,40,50,60]
for item in cart:
     if item>=100:
         print("we can not process this item:",item)
         continue
     print(item)
     