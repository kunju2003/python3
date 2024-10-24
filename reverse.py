n=int(input("enter a number:"))
r=0
while n>0:
    rem=n%10
    r=(r*10)+rem
    n=n//10

print("reverse of number",r)
