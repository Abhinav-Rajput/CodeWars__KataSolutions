# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contains any char.
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    countx=0
    counto=0
    for i in s:
        if 'x' in i or 'X' in i:
            countx += 1
        elif 'o' in i or 'O' in i:
            counto += 1
    if countx == counto:
        return True
    else:
        return False

