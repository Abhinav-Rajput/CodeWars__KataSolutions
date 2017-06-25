def move_zeros(array):

    w = []
    d = 0

    for i in array:
        if i is False:
            w.append(False)
        elif i == 0:
            d += 1
        else:
            w.append(i)
    for i in range(0, d):
        w.append(0)

    print (w)
    return w

def main():
    pass

if __name__ == '__main__':
    main()    
