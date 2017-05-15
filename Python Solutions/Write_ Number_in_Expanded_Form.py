# Write Number in Expanded Form

# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'


def expanded_form(num):
    strNum = str(num)
    line = ''
    space=' '
    for i in range(0,len(strNum)):
        if strNum[i]=='0':
            continue
        line += strNum[i] + ''
        for j in range(0,(len(strNum)-(i+1))):
            line += '0'
        line += ' + '
            
    line = line[0:len(line)-3]
    return line