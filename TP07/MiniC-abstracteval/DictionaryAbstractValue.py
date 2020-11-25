import copy
from SignatureAbstractValue import AbstractValue
from SignatureLatticeElement import Bot

########################################
###### DICTIONARY ABSTRACT DOMAIN ######
########################################

class DictionaryAbstractValue(AbstractValue):
    """
    An abstract value which is the cross product of single elements (pointwise)
    implemented as a dict from id to ArithmeticLatticeElements.
    """

    def __init__(self, LE, init=None):
        self._latElem = LE
        self._isBot = False
        self._tempVars = set()
        self._tempCounter = 0
        if init is not None:
            self._values = init
            self._progVars = init.keys()
        else:
            self._values = dict()  # id -> LatticeElement
            self._progVars = set()

    # Predicates
    def isBot(self):
        return self._isBot

    # About variables
    def newVar(self, varName):
        self._progVars.add(varName)
        self._values[varName] = self._latElem.top()  # Undefined behavior is top()

    def _newTemp(self):
        tempName = "TEMP#" + str(self._tempCounter)  # We assume this cannot be a standard variable name
        self._tempCounter += 1
        self._tempVars.add(tempName)
        self._values[tempName] = self._latElem.top()  # Undefined behavior is top()
        return tempName

    def _eraseTemp(self, tempName):
        if tempName in self._tempVars:
            self._tempVars.remove(tempName)
            del self._values[tempName]

    # About copying
    def copy(self):
        cp = copy.deepcopy(self)
        return cp

    def topCopy(self):
        cp = self.copy()
        cp._isBot = False
        to_erase = self._tempVars.copy()
        for var in to_erase:
            cp._eraseTemp(var)
        for var in self._progVars:
            cp._abstractAssignTop(var)
        return cp

    def botCopy(self):
        cp = self.topCopy()
        cp._isBot = True
        return cp

    def _override(self, newself):
        cp = newself.copy()
        self._latElem = cp._latElem
        self._isBot = cp._isBot
        self._tempVars = cp._tempVars
        self._progVars = cp._progVars
        self._values = cp._values
        self._tempCounter = cp._tempCounter

    # About accessing and changing information
    def getVal(self, varName, erase_temp=False):
        val = self._values[varName]
        if erase_temp:
            self._eraseTemp(varName)
        if self.isBot():
            return Bot()
        else:
            return val

    def abstractAssign(self, varName, ident):
        if self.isBot():
            return
        else:
            val = self.getVal(ident,True)
            self._values[varName] = val


    def _abstractAssignTop(self, varName):
        self._values[varName] = self._latElem.top()

    def _abstractAssignBot(self, varName):
        self._override(self.botCopy())
        self._values[varName] = self._latElem.top()

    def _abstractAssignVal(self, varName, val):
        if val.isBot():
            self._abstractAssignBot(varName)
        else:
            self._values[varName] = val

    # Lattive operations. They ignore variables that are not in _progVars
    def _pointwise(self, other, f):
        for var in self._progVars:
            val = f(self._values[var], other._values[var])
            self._abstractAssignVal(var,val)

    def join(self, other):
        """"
        Pointwise join for dicts of Abstract Values of the same type
        """
        if self.isBot():  # Join with bottom is the other
            self._override(other)
        elif other.isBot():
            pass
        else:
            self._pointwise(other, lambda x, y: x.join(y))

    def meet(self, other):
        """
        Pointwise meet for dicts of Abstract Values of the same type
        """
        if self.isBot():  # Meet with bottom is bottom
            pass
        elif other.isBot():
            self._override(other)
        else:
            self._pointwise(other, lambda x, y: x.meet(y))

    def widen(self, other):
        if self.isBot():  # Widen with bottom is the other (like join)
            self._override(other)
        elif other.isBot():
            pass
        else:
            self._pointwise(other, lambda x, y: x.widen(y))

    def rev_widen(self, other):
        if self.isBot():  # Widen with bottom is the other (like join)
            self._override(other)
        elif other.isBot():
            pass
        else:
            self._pointwise(other, lambda x, y: y.widen(x))

    def below(self, other):
        if self.isBot():
            return True
        if other.isBot():
            return False
        for var, sval in self._values.items():
            oval = other._values[var]
            if not sval.below(oval):
                return False
        return True

    def equal(self, other):
        return self.below(other) and other.below(self)

    # The following methods take as input the variable containing the operands of the computation
    # And return a newly created temporary variable for the result

    def _abstractBinaryOp(self, n1, n2, f):
        tres = self._newTemp()
        v1 = self.getVal(n1,True)
        v2 = self.getVal(n2,True)
        if not self.isBot():
            res = f(v1, v2)
            self._abstractAssignVal(tres,res)
            return tres
        self._abstractAssignBot(tres)
        return tres

    def _abstractUnaryOp(self, n, f):
        tres = self._newTemp()
        v = self.getVal(n,True)
        if not self.isBot():
            res = f(v)
            self._abstractAssignVal(tres,res)
            return tres
        self._abstractAssignBot(tres)
        return tres

    def _abstractConstantOp(self, c):
        tres = self._newTemp()
        if not self.isBot():
            res = c
            self._abstractAssignVal(tres,res)
            return tres
        self._abstractAssignBot(tres)
        return tres

    # Lattice constant
    def abstractTop(self):
        return self._abstractConstantOp(self._latElem.top())

    def abstractBot(self):
        self._override(self.botCopy())
        return self._abstractConstantOp(self._latElem.top())

    # Arithmetic operations
    def abstractInt(self, n):
        return self._abstractConstantOp(self._latElem.ofInt(n))

    def abstractUnaryMinus(self, n):
        return self._abstractUnaryOp(n, lambda x: -x)

    def abstractAdd(self, n1, n2):
        return self._abstractBinaryOp(n1, n2, lambda x, y: x + y)

    def abstractSub(self, n1, n2):
        return self._abstractBinaryOp(n1, n2, lambda x, y: x - y)

    def abstractMult(self, n1, n2):
        return self._abstractBinaryOp(n1, n2, lambda x, y: x * y)

    def abstractDiv(self, n1, n2):
        #print("HERE",self.getVal(n2, False),self.getVal(n2, False).isZero())
        war = self.getVal(n2, False).isZero() if not self.isBot() else False
        res = self._abstractBinaryOp(n1, n2, lambda x, y: x / y)
        return war, res

    def abstractMod(self, n1, n2):
        war = self.getVal(n2, False).isZero()  if not self.isBot() else False
        res = self._abstractBinaryOp(n1, n2, lambda x, y: x % y)
        return war, res

    def abstractRand(self, n1, n2):
        return self._abstractBinaryOp(n1, n2, lambda x, y: x.interval(y))

    def abstractRel(self, n1, R, n2):
        case_true = self.copy()
        case_false = self.copy()
        v1 = self.getVal(n1,True)
        v2 = self.getVal(n2,True)
        if self.isBot():
            return self.copy(),self.copy()
        assert(not v1.isBot())
        assert(not v2.isBot())
        # We extract "what do we lear from n1 and n2 if the condition is true or false"
        linfo_true,rinfo_true = R.apply(v1,v2)
        linfo_false,rinfo_false = R.neg().apply(v1,v2)
        # We create two states: "what happens if true" and "what happens if false"
        case_true._abstractAssignVal(n1,linfo_true)
        case_true._abstractAssignVal(n2,rinfo_true)
        case_false._abstractAssignVal(n1,linfo_false)
        case_false._abstractAssignVal(n2,rinfo_false)
        # We clean temporary variables
        # This means that we don't gain any information if the condition is not "var R expr" or "expr R var"
        case_true._eraseTemp(n1)
        case_false._eraseTemp(n1)
        case_true._eraseTemp(n2)
        case_false._eraseTemp(n2)
        return case_true,case_false

    def __repr__(self):
        b = "⊥" if self._isBot else "_"
        return "AVM({} {})".format(b, self._values)

    def __str__(self):
        b = "⊥" if self._isBot else "_"
        return "AVM({} {})".format(b, self._values)

