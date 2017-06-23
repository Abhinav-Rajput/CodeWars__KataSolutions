import math
class Vector():

    def __init__(self,tab):
        self.tab = tab

    def add(self,v):
        if(len(self.tab)!=len(v.tab)):
            raise ValueError("This is mistake!")
        table = [None]*len(self.tab)
        a = Vector(table)

        for i in range(len(self.tab)):
            a.tab[i] = self.tab[i] + v.tab[i]

        print(a.tab)
        return a

    def subtract(self,v):
        table = [None] * len(self.tab)
        a = Vector(table)

        for i in range(len(self.tab)):
            a.tab[i] = self.tab[i] - v.tab[i]

        print(a.tab)
        return a

    def dot(self,v):
        sum = self.tab[0]*v.tab[0]
        for i in range(1,len(self.tab)):
            sum += self.tab[i]*v.tab[i]

        print(sum)
        return sum

    def norm(self):
        sum = 0
        for x in self.tab:
            sum+=x**2

        print(math.sqrt(sum))
        return math.sqrt(sum)

    def __str__(self):
        s = "("
        i = 0;
        while i < len(self.tab):
            s += str(self.tab[i])
            if i != len(self.tab) - 1:
                s += ","
            i += 1
        s+=")"
        print(s)
        return s

    def equals(self, v):
        return (self.tab == v.tab)