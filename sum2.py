nsum=0
esum=0
osum=0
i=1
while i<=10:
    nsum+=i
    if i%2==0:
        esum+=i
    elif i%2!=0:
        osum+=i
    i+=1
print("sum of nsum",nsum) 
print("sum of esum",esum)  
print("sum of osum",osum)    

