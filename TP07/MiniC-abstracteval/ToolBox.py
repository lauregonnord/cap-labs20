from MiniCParser import MiniCParser


###################################
########## VisitorOutput ##########
###################################


class VisitorOutput:
    """
    Store the results of the assertions in order to print them at the end.
    """
    def __init__(self,init=dict()):
        self._outputs = init

    def assertion_unreachable(self,ctx):
        """ assert at line N: unreachable """
        self._add(SingleVisitorOutput.assertion_unreachable(ctx))
    def assertion_verified(self,ctx):
        """ assert at line N: verified """
        self._add(SingleVisitorOutput.assertion_verified(ctx))
    def assertion_failed(self,ctx):
        """ assert at line N: failed to verify """
        self._add(SingleVisitorOutput.assertion_failed(ctx))

    def div_0(self,ctx):
        """ Warning div by 0 line {} """
        self._add(SingleVisitorOutput.div_0(ctx))
    def mod_0(self,ctx):
        """ Warning mod by 0 line {} """
        self._add(SingleVisitorOutput.mod_0(ctx))

    def print_stmt(self,ctx,val):
        """ any custom message """
        self._add(SingleVisitorOutput(ctx,val))

    def _add(self,svo):
        """ internal function used to add messages """
        self._outputs[(svo.line,svo.column)] = svo
    def display(self):
        """ print all stored outputs """
        for k in sorted(self._outputs.keys()):
            print(self._outputs[k])

class SingleVisitorOutput:
    """
    Class used by VisitorOutput to store single outputs.
    You should not need to read the content of this class.
    """
    W_DIV_0,W_MOD_0,A_VERIF,A_FAILED,A_UNR,OTHER = range(6)
    def __init__(self,ctx,init = None):
        self.ty = SingleVisitorOutput.OTHER
        self.line = ctx.start.line
        self.column = ctx.start.column
        self.content = init
    @classmethod
    def div_0(cls,ctx):
        o = cls(ctx);
        o.ty = SingleVisitorOutput.W_DIV_0
        return o
    @classmethod
    def mod_0(cls,ctx):
        o = cls(ctx);
        o.ty = SingleVisitorOutput.W_MOD_0
        return o
    @classmethod
    def assertion_unreachable(cls,ctx):
        o = cls(ctx);
        o.ty = SingleVisitorOutput.A_UNR
        return o
    @classmethod
    def assertion_verified(cls,ctx):
        o = cls(ctx);
        o.ty = SingleVisitorOutput.A_VERIF
        return o
    @classmethod
    def assertion_failed(cls,ctx):
        o = cls(ctx);
        o.ty = SingleVisitorOutput.A_FAILED
        return o
    def __str__(self):
           if self.ty == SingleVisitorOutput.W_DIV_0:
              return ("Warning div by 0 line {}".format(self.line))
           elif self.ty == SingleVisitorOutput.W_MOD_0:
              return ("Warning mod by 0 line {}".format(self.line))
           elif self.ty == SingleVisitorOutput.A_VERIF:
              return ("assert at line {}: verified".format(self.line))
           elif self.ty == SingleVisitorOutput.A_FAILED:
              return ("assert at line {}: failed to verify".format(self.line))
           elif self.ty == SingleVisitorOutput.A_UNR:
              return ("assert at line {}: unreachable".format(self.line))
           else:
              return str(self.content)



##############################
########## RELATION ##########
##############################

class Relation:
    """
    Contains all the different kind of comparison, and basic operations on relations.
    """
    LEQ, GEQ, EQ, GT, LT, NEQ = 1,2,3,-1,-2,-3
    def __init__(self,init):
       if init not in { Relation.LEQ, Relation.GEQ, Relation.EQ, Relation.GT, Relation.LT, Relation.NEQ }:
          raise Exception #Unknown comparison operator
       self._rel = init

    def neg(self):
       """ Opposite relation """
       return Relation(-self._rel)
   
    def isLEQ(self):
        return self._rel == Relation.LEQ
    def isLT(self):
        return self._rel == Relation.LT
    def isGEQ(self):
        return self._rel == Relation.GEQ
    def isGT(self):
        return self._rel == Relation.GT
    def isEQ(self):
        return self._rel == Relation.EQ
    def isNEQ(self):
        return self._rel == Relation.NEQ

    @classmethod
    def fromCtx(cls,ctx):
        """ extract from the MiniCParser which relation is in the context """
        R = ctx.myop.type
        if R == MiniCParser.LTEQ:
            return cls(Relation.LEQ)
        if R == MiniCParser.LT:
            return cls(Relation.LT)
        if R == MiniCParser.GT:
            return cls(Relation.GT)
        if R == MiniCParser.GTEQ:
            return cls(Relation.GEQ)
        if R == MiniCParser.EQ:
            return cls(Relation.EQ)
        if R == MiniCParser.NEQ:
            return cls(Relation.NEQ)
        raise Exception #Unknown comparison operator   
 
    def apply(self,x,y):
       """ apply a relation to its arguments """
       if self.isLEQ():
           return x <= y
       if self.isGEQ():
           return x >= y
       if self.isEQ():
           return x == y
       if self.isGT():
           return x > y
       if self.isLT():
           return x < y
       if self.isNEQ():
           return x != y
       raise Exception  #Unknown comparison operator  

    def __repr__(self):
       if self.isLEQ():
           return "≤"
       if self.isGEQ():
           return "≥"
       if self.isEQ():
           return "="
       if self.isGT():
           return ">"
       if self.isLT():
           return "<"
       if self.isNEQ():
           return "≠"
       raise Exception

