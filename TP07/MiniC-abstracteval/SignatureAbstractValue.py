# Python 3.6 is pretty bad at handling type annotations (contrary to Python 4),
# so I'm using comments instead of the importing Typing.

class AbstractValue:
    """
    Used to represent the current state of the program.
    This class only contain the description of the methods.
    Refer to the class DictionaryAbstractValue for an implementation
    simply storing for each variable an ArithmeticLatticeElement for its value,
    and applying all the operations pointwise.
    """

    def __init__(self):
        """
        Create a new abstract value for the program.
        Arguments of this method might vary on inherited classes.
        """
        raise NotImplementedError

    # Predicates
    def isBot(self):
        """
        AbstractValue -> bool
        Check if the abstract value is ⊥, i.e the empty abstract value.
        It corresponds to unreachable points of the program.
        """
        raise NotImplementedError

    # About variables
    def newVar(self, varName):
        """
        AbstractValue * string -> None
        Add a new variable to the abstract value, initialised at ⊤
        """
        raise NotImplementedError

    # About copying
    def copy(self):
        """
        AbstractValue -> AbstractValue
        Create a copy of the abstract value
        """
        raise NotImplementedError

    def topCopy(self):
        """
        AbstractValue -> AbstractValue
        Create a copy of the abstract value, where all information is forgotten and every variable to ⊤
        """
        raise NotImplementedError

    def botCopy(self):
        """
        AbstractValue -> AbstractValue
        Create a copy of the abstract value, where all information is forgotten and every variable to ⊥
        """
        raise NotImplementedError

    # About accessing and changing information
    def getVal(self, varName):
        """
        AbstractValue * str -> None
        Return the value of the variable varName.
        Apart for debugging purposes, you should not need this method.
        """
        raise NotImplementedError

    def abstractAssign(self, varNameReceiving, varNameSending):
        """
        AbstractValue * str * str -> None
        Assign to the variable varNameReceiving the value contained in varNameSending.
        Update the abstract value with the result.
        """
        raise NotImplementedError

    # Lattice operations
    def join(self, other):
        """
        AbstractValue * AbstractValue -> None
        Make a join (union) of two abstract values.
        Update the first with the result.
        """
        raise NotImplementedError

    def meet(self, other):
        """
        AbstractValue * AbstractValue -> None
        Make a meet (intersection) of two abstract values.
        Update the first with the result.
        """
        raise NotImplementedError

    def widen(self, other):
        """
        AbstractValue * AbstractValue -> None
        Make a widening of the first abstract value by the second one.
        Update the first with the result.
        """
        raise NotImplementedError

    def rev_widen(self, other):
        """
        AbstractValue * AbstractValue -> None
        Make a widening of the second abstract value by the first one.
        Update the first with the result.
        """
        raise NotImplementedError

    def below(self, other):
        """
        AbstractValue * AbstractValue -> bool
        Check if the first abstract value is included in the second one.
        """
        raise NotImplementedError

    def equal(self, other):
        """
        AbstractValue * AbstractValue -> bool
        Check if the first abstract value is equal to the second one.
        """
        raise NotImplementedError

    # The following methods take as input the variable containing the operands of the computation
    # And return a newly created temporary variable for the result
    # Lattice constant
    def abstractTop(self):
        """
        AbstractValue -> str
        Create a new temporary variable containing ⊤
        """
        raise NotImplementedError

    def abstractBot(self):
        """
        AbstractValue -> str
        Create a new temporary variable containing ⊥
        """
        raise NotImplementedError

    # Arithmetic operations
    def abstractInt(self, n):
        """
        AbstractValue * int -> str
        Create a new temporary variable containing the integer n
        """
        raise NotImplementedError

    def abstractUnaryMinus(self, n):
        """
        AbstractValue * str -> str
        Create a new temporary variable containing the negation of the argument
        """
        raise NotImplementedError

    def abstractAdd(self, n1, n2):
        """
        AbstractValue * str * str -> str
        Create a new temporary variable containing the addition of the arguments
        """
        raise NotImplementedError

    def abstractSub(self, n1, n2):
        """
        AbstractValue * str * str -> str
        Create a new temporary variable containing the difference of the arguments
        """
        raise NotImplementedError

    def abstractMult(self, n1, n2):
        """
        AbstractValue * str * str -> str
        Create a new temporary variable containing the multiplication of the arguments
        """
        raise NotImplementedError

    def abstractDiv(self, n1, n2):
        """
        AbstractValue * str * str -> bool * str
        Return a boolean true if a division by zero is possible
        Create a new temporary variable containing the quotient of the arguments.
        """
        raise NotImplementedError

    def abstractMod(self, n1, n2):
        """
        AbstractValue * str * str -> bool * str
        Return a boolean true if a modulo by zero is possible
        Create a new temporary variable containing the modulo of the arguments.
        """
        raise NotImplementedError

    def abstractRand(self, n1, n2):
        """
        AbstractValue * str * str -> str
        Create a new temporary variable containing the result of "rand" applied to the arguments
        """
        raise NotImplementedError

    def abstractRel(self, n1, R, n2):
        """
        AbstractValue * str * Relation * str -> AbstractValue * AbstractValue
        Study the relation "n1 R n2", and return "state if it is true" and "state if it is false".
        To check if the relation is always true, use the isBot() method on the second output.
        To check if the relation is always false, use the isBot() method on the first output.
        """
        raise NotImplementedError
