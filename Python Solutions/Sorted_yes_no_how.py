# Implement the method isSortedAndHow, which accepts an array of integers, and returns one of the following:

# 'yes, ascending' - if the numbers in the array are sorted in an ascending way
# 'yes, descending' - if the numbers in the array are sorted in a descending way
# 'no'
# You can assume the array will always be valid, and there will always be one correct answer.


def is_sorted_and_how(arr):
    #your code here
    ascending = True
    descc = True
    previous =   arr[0]
    for number in arr:
        if number < previous:
            ascending = False
        previous = number
    if ascending== False:
        previous = arr[0]
        for number in arr:
            if number > previous:
                descc = False
            previous = number 
        if descc == False:
            return 'no'
        elif descc == True:
            return 'yes, descending'
    elif ascending == True:
        return 'yes, ascending'