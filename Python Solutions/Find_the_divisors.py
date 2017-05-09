# Create a function named divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). 
# If the number is prime return the string '(integer) is prime' (use Either String a in Haskell).
# Example:

# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

def divisors(integer):
    l=[]
    flag=0
    for i in range(2,integer):
        if(integer%i)==0:
            l.append(i)
            flag=1                
    if flag==0:
        return str(integer)+" is prime"
    else:
        return l
        