# Python 3.6 is pretty bad at handling type annotations (contrary to Python 4),
# so I'm using comments instead of the importing Typing.

class Bot:
    def __init__(self):
       pass
    def isBot(self):
        return True
    def copy(self):
        return Bot()
    def __str__(self):
       return "⊥"
    def __repr__(self):
       return "⊥"
   

class LatticeElement:

    def __init__(self,init = None):
        """
        Yield the universal ⊤ element unless provided with an argument.
        The element ⊥ is not treated withing this class.
        """
        self._repr = init

    def __repr__(self):
        """
        String representation of the lattice element.
        """
        if self.isTop():
           return "⊤"
        return self._repr.__repr__()

    def isTop(self):
        """
        LatticeElement -> bool
        Test if the lattice element is ⊤.
        """
        return self._repr is None
    def isBot(self):
        """
        LatticeElement -> bool
        Test if the lattice element is ⊥.
        Since ⊥ is handled by the class Bot, always return False.
        """
        return False
    def isVal(self):
        """
        LatticeElement -> bool
        Test if the lattice element is neither ⊤ or ⊥.
        """
        return self._repr is not None
    @classmethod
    def top(cls):
        """
        Class -> LatticeElement
        Build the lattice element ⊤.
        """
        return cls()
    @classmethod
    def bot(cls):
        """
        Class -> LatticeElement
        Build the lattice element ⊥.
        """
        return Bot()
    @classmethod
    def ofVal(cls,val):
        """
        Class * anything -> LatticeElement
        Build the lattice element of a value.
        """
        return cls(val)
    def getVal(self):
        """
        Class * anything -> LatticeElement
        Extract the value of a lattice element.
        Return None if ⊤ or ⊥.
        """
        return self._repr

    def copy(self):
        """
        LatticeElement -> LatticeElement
        Make a copy of the lattice element.
        """
        return self.top() if self.isTop() else self.ofVal(self.getVal())

    def join(self,other):
        """
        LatticeElement * LatticeElement -> LatticeElement
        Compute the join (= union) of two lattice elements.
        REMINDER: should be overridden in inheriting classes.
        """
        if self.isTop() or other.isTop():
           return self.top()
        else:
           raise NotImplementedError
    def meet(self,other):
        """
        LatticeElement * LatticeElement -> LatticeElement
        Compute the meet (= intersection) of two lattice elements.
        REMINDER: should be overridden in inheriting classes.
        """
        if self.isTop():
           return other.copy()
        if other.isTop():
           return self.copy()
        else:
           raise NotImplementedError
    def widen(self,other):
        """
        LatticeElement * LatticeElement -> LatticeElement
        Compute the widening of two lattice elements.
        On finite height lattices, this is simply the join.
        REMINDER: should be overridden in inheriting classes of infinite height.
        """
        return self.join(other)
    def below(self,other):
        """
        LatticeElement * LatticeElement -> bool
        Return true if and only if self ⊆ other.
        REMINDER: should be overridden in inheriting classes.
        """
        if other.isTop():
            return True
        if self.isTop():
            return False
        raise NotImplementedError


class ArithmeticLatticeElement(LatticeElement):
    @classmethod
    def ofInt(cls,n):
        """
        Class * int -> ArithmeticLatticeElement
        Build the smallest lattice element containing an integer.
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError
    def isInt(self):
        """
        ArithmeticLatticeElement -> bool
        Test if the lattice element is a singleton containing an integer.
        REMINDER: should be overridden in inheriting classes.
        """
        if not self.isVal():
           return False
        raise NotImplementedError
    def getInt(self):
        """
        ArithmeticLatticeElement -> int
        Extract the integer corresponding to a lattice element.
        Return None if it is not a singleton.
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError
    def isZero(self):
        """
        ArithmeticLatticeElement -> bool
        Test if the lattice element contains zero.
        Will be used for testing division by zero.
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError

    def __add__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement
        Infix operator +
        REMINDER: should be overridden in inheriting classes.
        """         
        if self.isTop() or other.isTop():
            return self.top()
        raise NotImplementedError
    def __sub__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement
        Infix operator -
        REMINDER: should be overridden in inheriting classes.
        """         
        if self.isTop() or other.isTop():
            return self.top()
        raise NotImplementedError
    def __mul__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement
        Infix operator *
        REMINDER: should be overridden in inheriting classes.
        """         
        if self.isTop() or other.isTop():
            return self.top()
        raise NotImplementedError
    def __truediv__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement
        Infix operator /
        We chose to always return ⊤
        """
        return self.top()
    def __mod__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement
        Infix operator %
        We chose to always return ⊤
        """
        return self.top()
    def __neg__(self):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement
        Unary operator -
        REMINDER: should be overridden in inheriting classes.
        """         
        if self.isTop():
            return self.top()
        raise NotImplementedError
    def interval(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement
        Compute the element corresponding to the interval [self,other]
        REMINDER: should be overridden in inheriting classes.
        """
        if self.isTop() or other.isTop():
            return self.top()
        raise NotImplementedError

    def __le__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement * ArithmeticLatticeElement
        Infix operator <=, should return a pair corresponding:
        + The updated state of the left-hand-side assuming the statement is true
        + The updated state of the right-hand-side assuming the statement is true
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError
    def __lt__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement * ArithmeticLatticeElement
        Infix operator <, should return a pair corresponding:
        + The updated state of the left-hand-side assuming the statement is true
        + The updated state of the right-hand-side assuming the statement is true
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError
    def __ge__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement * ArithmeticLatticeElement
        Infix operator >=, should return a pair corresponding:
        + The updated state of the left-hand-side assuming the statement is true
        + The updated state of the right-hand-side assuming the statement is true
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError
    def __gt__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement * ArithmeticLatticeElement
        Infix operator >, should return a pair corresponding:
        + The updated state of the left-hand-side assuming the statement is true
        + The updated state of the right-hand-side assuming the statement is true
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError
    def __eq__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement * ArithmeticLatticeElement
        Infix operator ==, should return a pair corresponding:
        + The updated state of the left-hand-side assuming the statement is true
        + The updated state of the right-hand-side assuming the statement is true
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError
    def __ne__(self,other):
        """
        ArithmeticLatticeElement * ArithmeticLatticeElement -> ArithmeticLatticeElement * ArithmeticLatticeElement
        Infix operator !=, should return a pair corresponding:
        + The updated state of the left-hand-side assuming the statement is true
        + The updated state of the right-hand-side assuming the statement is true
        REMINDER: should be overridden in inheriting classes.
        """
        raise NotImplementedError


