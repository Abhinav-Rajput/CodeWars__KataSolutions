# Tribonacci Sequence

def tribonacci(signature,n):
    #your code here
    e=[]
    if n==0:
        return e
    else:
        a=signature[0]
        b=signature[1]
        c=signature[2]
        d=[]
        d.append(a)
        if n==1:
            return d
        d.append(b)            
        if n==2:
            return d        
        d.append(c)
        for i in range(3,n):
            e=a+b+c
            d.append(e)
            a=b
            b=c
            c=e
        return d