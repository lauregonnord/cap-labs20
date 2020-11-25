from SignatureLatticeElement import ArithmeticLatticeElement

class Sign:
    Neg = -1
    Pos = +1
    Zero = 0

class SignLatticeElement(ArithmeticLatticeElement):
    # We start by overriding the lattice operations, except widen since sign is of finite height.
    def join(self,other):
        if self.isTop() or other.isTop():
           return self.top()
        elif self.getVal() == other.getVal():
            return self.copy()
        else:
            return self.top()
    def meet(self,other):
        if self.isTop():
            return other.copy()
        elif other.isTop():
            return self.copy()
        elif self.getVal() == other.getVal():
            return self.copy()
        else:
            return self.bot()
    def below(self,other):
        if other.isTop():
            return True
        elif self.getVal() == other.getVal():
            return True
        else:
            return False

    # We now override the arithmetic operations.
    ## We take care of conversions to and from integers
    @classmethod
    def ofInt(cls, n):
        if n > 0:
            v = Sign.Pos
        elif n < 0:
            v = Sign.Neg
        else:
            v = Sign.Zero
        return cls.ofVal(v)
    def isInt(self):
        return self.getVal() == Sign.Zero
    def getInt(self):
        if self.isInt():
            return 0
        else:
            return None
    def isZero(self):
        return self.isTop() or self.getVal() == Sign.Zero
    ## We take care of +,-,*,interval
    def __add__(self,other):
        if self.getVal() == Sign.Zero:
            return other.copy()
        elif other.getVal() == Sign.Zero:
            return self.copy()
        elif self.getVal() == other.getVal():
            return self.copy()
        else:
            return self.top()
    def __neg__(self):
        if self.isTop():
            return self.copy()
        else:
            return self.ofVal(-self.getVal())
    def __sub__(self, other):
        return self + (- other)
    def __mul__(self,other):
        if self.getVal() == Sign.Zero or other.getVal() == Sign.Zero:
            return self.ofVal(Sign.Zero)
        if self.isTop() or other.isTop():
            return self.top()
        return self.ofVal(self.getVal()*other.getVal())
    def interval(self,other):
        if self.isTop() or other.isTop():
            return self.top()
        elif self.getVal() == other.getVal():
            return self.copy()
        elif self.getVal() < other.getVal():
            return self.top()
        else:
            return self.bot()
    ## We take care of all the comparison.
    ## They output what happens to left/right hand side if we assume the comparison is true
    def __eq__(self,other):
        if self.isTop():
            return other.copy(),other.copy()
        elif other.isTop():
            return self.copy(),self.copy()
        elif self.getVal() == other.getVal():
            return self.copy(),other.copy()
        else:
            return self.bot(),other.bot()
    def __ne__(self,other):
        if self.getVal() == Sign.Zero and other.getVal() == Sign.Zero:
            return self.bot(),other.bot()
        else:
            return self.copy(),other.copy()
    def __le__(self, other):
        if other.getVal() == Sign.Neg:
            # x <= Neg implies x Neg
            if self.getVal() == Sign.Zero or self.getVal() == Sign.Pos:
                return self.bot(),other.bot()
            else:
                return self.ofVal(Sign.Neg),other.copy()
        elif other.getVal() == Sign.Zero:
            # x <= Zero implies x not Neg
            if self.getVal() == Sign.Pos:
                return self.bot(),other.bot()
            else:
                return self.copy(),other.copy()
        elif other.getVal() == Sign.Pos:
            # x <= Pos implies nothing
            return self.copy(),other.copy()
        elif other.isTop():
            if self.getVal() == Sign.Neg:
                # Neg <= x implies nothing
                return self.copy(),other.copy()
            elif self.getVal() == Sign.Zero:
                # Zero <= x implies x not Neg
                return self.copy(),other.copy()
            elif self.getVal() == Sign.Pos:
                # Pos <= x implies x Pos
                return self.copy(),other.ofVal(Sign.Pos)
            elif self.isTop():
                return self.top(),other.top()
            else:
                #print(self,other)
                raise Exception # "other" is Bot, which should never happen
        else:
            #print(self,other)
            raise Exception # "other" is Bot, which should never happen
    def __lt__(self, other):
        if other.getVal() == Sign.Neg or other.getVal() == Sign.Zero:
            # x < Neg or Zero implies x Neg
            if self.getVal() == Sign.Zero or self.getVal() == Sign.Pos:
                return self.bot(),other.bot()
            else:
                return self.ofVal(Sign.Neg),other.copy()
        elif other.getVal() == Sign.Pos:
            # x < Pos implies nothing
            return self.copy(),other.copy()
        elif other.isTop():
            if self.getVal() == Sign.Neg:
                # Neg < x implies nothing
                return self.copy(),other.copy()
            elif self.getVal() == Sign.Zero or self.getVal() == Sign.Pos:
                # Zero or Pos < x implies x Pos
                return self.copy(),other.ofVal(Sign.Pos)
            elif self.isTop():
                return self.top(),other.top()
            else:
                #print(self,other)
                raise Exception # "other" is Bot, which should never happen
        else:
            #print(self,other)
            raise Exception # "other" is Bot, which should never happen
    def __ge__(self,other):
        o,s = other <= self
        return s,o
    def __gt__(self,other):
        o,s = other < self
        return s,o

    def __repr__(self):
        if self.isTop():
            return "⊤"
        elif self.getVal() == Sign.Zero:
            return "0"
        elif self.getVal() == Sign.Pos:
            return "⊕"
        elif self.getVal() == Sign.Neg:
            return "⊖"
        else:
            raise Exception

