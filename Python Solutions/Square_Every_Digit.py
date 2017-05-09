# square every digit of a number.

# For example, if we run 9119 through the function, 811181 will come out.

# Note: The function accepts an integer and returns an integer
def square_digits(num):
    s=''
    l=[]
    while num>10:
        n = num%10
        num = int(num/10)
        s+= str(n*n)+','
        if num<10:
            s+= str(num*num)
            l=s.split(",")  
            l.reverse()
            s=''.join(l)
            return int(s)       