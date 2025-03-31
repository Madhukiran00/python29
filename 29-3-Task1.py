num=987654321
des_no=True
prev=num%10
while num!=0:
    last=num%10
    
    if prev>last:
        des_no=False
        break
    prev=last
    num=num//10
    
if des_no:
    print("The number is descending order")
    
else:
    print("The number is not in descending order ")
    