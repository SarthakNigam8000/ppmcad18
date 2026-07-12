def cal():
    a=10
    b=22
    c=a*b
    return c
    
output= cal()
print(output)

def cal():
    a=10
    b=22
    c=a*b
    return c,a,b
    
output= cal()
print(output)

def cal(a,b,c):
    return a*b*c
    

print(cal(10,20,30))
