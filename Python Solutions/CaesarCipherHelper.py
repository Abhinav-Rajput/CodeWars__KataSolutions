class CaesarCipher(object):
    def __init__(self, shift):
        self._shift = shift
        self._output = ''

    def encode(self, str):
        str = str.upper()
        self._output = ''
        stayInAlphabet = 0
        for ch in str:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + self._shift
                if stayInAlphabet > ord('Z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                self._output += finalLetter
            else:
                self._output += ch
        print(self._output)
        return self._output

    def decode(self, str):
        str = str.upper()
        self._output = ''
        stayInAlphabet = 0
        for ch in str:
            if ch.isalpha():
                stayInAlphabet = ord(ch) - self._shift
                if stayInAlphabet < ord('A'):
                    stayInAlphabet += 26
                finalLetter = chr(stayInAlphabet)
                self._output += finalLetter
            else:
                self._output += ch
        print(self._output)
        return self._output


def main():
    c = CaesarCipher(5)
    print(c.encode('Codewars') == 'HTIJBFWX')
    print(c.decode('HTIJBFWX') == 'CODEWARS')


if __name__ == '__main__':
    main()
