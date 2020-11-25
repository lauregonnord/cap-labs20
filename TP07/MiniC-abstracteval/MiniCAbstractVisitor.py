from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from ToolBox import Relation,VisitorOutput
from SignatureLatticeElement import Bot

debug = False

class MiniCInternalError(Exception):
    pass


def execute_abstract_interpretation(program,abstract_domain,debug_enabled):
    """
    Take as an input the tree of the program,
    the abstract domain (i.e. a class inheriting from AbstractValue)
    and a boolean for enabling debug more.
    Should output an element of the class VisitorOutput()
    """
    outputs = VisitorOutput()
    global debug
    debug = debug_enabled
    assertCollector = AssertCollector(outputs)
    assertCollector.visit(program)
    visitor = MiniCAbstractVisitor(abstract_domain, outputs)
    try:
        visitor.visit(program)
    except MiniCInternalError as e:
        print(e.args[0])
        exit(2)
    return outputs


# Collect the assert and initialise them
class AssertCollector(MiniCVisitor):
    def __init__(self, out):
        self._outputs = out

    def visitAssertStat(self, ctx):
        """ At the beginning all assertions are set to unreachable """
        self._outputs.assertion_unreachable(ctx)

    def visitPrintintStat(self, ctx):
        self._outputs.print_stmt(ctx,Bot())


class MiniCAbstractVisitor(MiniCVisitor):

    # AbsVal should be of a class inheriting from AbstractValue,
    # e.g DictionaryAbstractValue(SignLatticeElement)
    def __init__(self, AbsVal, outputs):
        self._memory = AbsVal
        self._outputs = outputs

    def visitAssertStat(self, ctx):
        self._outputs.assertion_unreachable(ctx)

    def visitVarDecl(self, ctx):
        raise NotImplementedError

    def visitBasicType(self, ctx):
        if not ctx.mytype.type == MiniCParser.INTTYPE:
            raise Exception("only integer variables are supported")

    def visitIdList(self, ctx):
        raise NotImplementedError

    def visitIdListBase(self, ctx):
        raise NotImplementedError


# integer expressions
    def visitNumberAtom(self, ctx):
        raise NotImplementedError

    def visitIdAtom(self, ctx):
        raise NotImplementedError

    def visitUnaryMinusExpr(self, ctx):
        raise NotImplementedError

    def visitAdditiveExpr(self, ctx):
        raise NotImplementedError

    def visitMultiplicativeExpr(self, ctx):
        raise NotImplementedError

    def visitParExpr(self, ctx):
        raise NotImplementedError

# statements

    def visitAssignStat(self, ctx):
        raise NotImplementedError

    def visitRandExpr(self, ctx):
        raise NotImplementedError

    def visitRelationalExpr(self, ctx):
        raise NotImplementedError

    def visitCondBlock(self, ctx):
        raise NotImplementedError

    def visitIfStat(self, ctx):
        raise NotImplementedError

    def oneLoopIteration(self,ctx):
        raise NotImplementedError

    def visitWhileStat(self, ctx):
        raise NotImplementedError

    def visitPrintintStat(self, ctx):
        raise NotImplementedError

    # Booleans

    def visitAndExpr(self, ctx):
        raise NotImplementedError

    def visitOrExpr(self, ctx):
        raise NotImplementedError

    def visitNotExpr(self, ctx):
        raise NotImplementedError

    def visitBooleanAtom(self, ctx):
        raise NotImplementedError

    # Float
    def visitPrintfloatStat(self, ctx):
        raise NotImplementedError

    # Strings
    def visitStringAtom(self, ctx):
        raise NotImplementedError

    def visitPrintstringStat(self, ctx):
        raise NotImplementedError

    # Array
    def visitArrayAllocExpr(self, ctx):
        raise NotImplementedError

    def visitArrayReadExpr(self, ctx):
        raise NotImplementedError

    def visitArrayWriteStat(self, ctx):
        raise NotImplementedError

    def visitArrayType(self, ctx):
        raise NotImplementedError

    # Function
    def visitFuncCall(self, ctx):
        raise NotImplementedError

    # For loop
    def visitForForStat(self, ctx):
        raise NotImplementedError

    def visitCpt(self, ctx):
        raise NotImplementedError
