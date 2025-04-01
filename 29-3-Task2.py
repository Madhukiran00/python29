num=831342543
temp=num
req_no=3
count=0
len=0
lis=[]
while num!=0:
    num=num//10
    len=len+1
    

while temp!=0:
    last_no=temp%10
    if last_no==req_no:
        lis.append(len)
        count=count+1
    len=len-1
    temp=temp//10
    
print(f"The {req_no} is present in {lis} positions")
print(f"The {req_no} is {count} times repeated")
