def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
num=input("Enter num")
a=[]
for i in range(num):
    n=input("Enter Num")
    a.append(n)

print(add(*a))


