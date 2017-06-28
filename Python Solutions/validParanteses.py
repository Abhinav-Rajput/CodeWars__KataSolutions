def valid_parentheses(string):
    #your code here
    count = 0
    for i in string:
        if i == '(':
            count+=1
        elif i == ')':
            count-=1
        if count<0:
            return False
    if count == 0:
        return True
    else :
        return False

def main():
    valid_parentheses("()")

if __name__ == '__main__':
    main()