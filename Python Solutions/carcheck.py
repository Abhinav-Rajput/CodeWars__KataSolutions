# charCheck("Cara Hertz", 10, True) should return [ True, "Cara Hertz" ]
# charCheck("Cara Hertz", 9, False) should return [ True, "CaraHertz" ]
# charCheck("Cara Hertz", 5, True) should return [ False, "Cara " ]
# charCheck("Cara Hertz", 5, False) should return [ False, "CaraH" ]


def charCheck(text, mx, spaces):
    if spaces == True:
        if len(text) <= mx:
            return [True,text]
        else:
            return [False,text[0:mx]]
    else:
        text = text.replace(' ','')
        if len(text) <= mx:
            return [True, text]
        else:
            return [False, text[0:mx]]

def main():
    print(charCheck("I am applying for the role of Base Manager on Titan.", 60, True))


if __name__ == '__main__':
    main()