from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from .APIRiscV import (RiscVFunction, Condition)
from .Instruction3A import Label
from . import Operands
from antlr4.tree.Trees import Trees
from Errors import MiniCInternalError, MiniCUnsupportedError

"""
CAP, MIF08, three-address code generation + simple alloc
This visitor constructs an object of type "RiscVFunction".
"""


class MiniCCodeGen3AVisitor(MiniCVisitor):

    def __init__(self, debug, parser):
        super().__init__()
        self._parser = parser
        self._debug = debug
        self._functions = []
        self._current_function = None
        self._lastlabel = ""
        self.ctx_stack = []  # useful for nested ITE

    def get_functions(self):
        return self._functions

    def printRegisterMap(self):
        print("--variables to memory map--")
        for keys, values in self._memory.items():
            print(keys + '-->' + str(values))

    # handle variable decl

    def visitVarDecl(self, ctx):
        type_str = ctx.typee().getText()
        vars_l = self.visit(ctx.id_l())
        for name in vars_l:
            if name in self._memory:
                raise MiniCInternalError(
                    "Variable {} has already been declared".format(name))
            else:
                tmp = self._current_function.new_tmp()
                self._memory[name] = tmp
                if type_str not in ("int", "bool"):
                    raise MiniCUnsupportedError("Unsupported type " + type_str)
                # Initialization to 0 or False, both represented with 0
                self._current_function.addInstructionLI(tmp, 0)

    def visitIdList(self, ctx):
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx):
        return [ctx.ID().getText()]

    # expressions

    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx):
        val = int(ctx.getText())
        dr = self._current_function.new_tmp()
        self._current_function.addInstructionLI(dr, val)
        return dr

    def visitFloatAtom(self, ctx):
        raise MiniCUnsupportedError("float literal")

    def visitBooleanAtom(self, ctx):
        # true is 1 false is 0
        b = ctx.getText()
        dr = self._current_function.new_tmp()
        if b == 'true':
            val = 1
        else:
            val = 0
        self._current_function.addInstructionLI(dr, val)
        return dr

    def visitIdAtom(self, ctx):
        try:
            # get the temporary associated to id
            return self._memory[ctx.getText()]
        except KeyError:
            raise Exception("Undefined variable {}, this should have failed to typecheck."
                            .format(ctx.getText()))

    def visitStringAtom(self, ctx):
        raise MiniCUnsupportedError("string atom")

    # now visit expressions : TODO

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitAdditiveExpr(self, ctx):
        tmpl = self.visit(ctx.expr(0))
        tmpr = self.visit(ctx.expr(1))
        dr = self._current_function.new_tmp()
        if ctx.myop.type == MiniCParser.PLUS:
            self._current_function.addInstructionADD(dr, tmpl, tmpr)
        else:
            self._current_function.addInstructionSUB(dr, tmpl, tmpr)
        return dr

    def visitOrExpr(self, ctx):
        tmpl = self.visit(ctx.expr(0))
        tmpr = self.visit(ctx.expr(1))
        dr = self._current_function.new_tmp()
        self._current_function.addInstructionOR(dr, tmpl, tmpr)
        return dr

    def visitAndExpr(self, ctx):
        tmpl = self.visit(ctx.expr(0))
        tmpr = self.visit(ctx.expr(1))
        dr = self._current_function.new_tmp()
        self._current_function.addInstructionAND(dr, tmpl, tmpr)
        return dr

    def visitEqualityExpr(self, ctx):
        return self.visitRelationalExpr(ctx)

    def visitRelationalExpr(self, ctx):
        c = Condition(ctx.myop.type)
        if self._debug:
            print("relational expression:")
            print(Trees.toStringTree(ctx, None, self._parser))
            print("Condition:", c)
        tmpl = self.visit(ctx.expr(0))
        tmpr = self.visit(ctx.expr(1))
        dest = self._current_function.new_tmp()
        end_relational = self._current_function.new_label('end_relational')
        self._current_function.addInstructionLI(dest, 0)
        self._current_function.addInstructionCondJUMP(
            end_relational, tmpl, c.negate(), tmpr)
        self._current_function.addInstructionLI(dest, 1)
        self._current_function.addLabel(end_relational)
        return dest

    def visitMultiplicativeExpr(self, ctx):
        div_by_zero_lbl = self._current_function.get_label_div_by_zero()
        tmpl = self.visit(ctx.expr(0))
        tmpr = self.visit(ctx.expr(1))
        dr = self._current_function.new_tmp()
        if ctx.myop.type == MiniCParser.MULT:
            self._current_function.addInstructionMUL(dr, tmpl, tmpr)
        elif ctx.myop.type == MiniCParser.DIV:
            self._current_function.addInstructionCondJUMP(
                div_by_zero_lbl, tmpr, Condition("beq"), 0)
            self._current_function.addInstructionDIV(dr, tmpl, tmpr)
        elif ctx.myop.type == MiniCParser.MOD:
            self._current_function.addInstructionCondJUMP(
                div_by_zero_lbl, tmpr, Condition("beq"), 0)
            self._current_function.addInstructionREM(dr, tmpl, tmpr)
        else:
            raise MiniCInternalError("Multiplicative expr, but not MUL|DIV|MOD?")
        return dr

    def visitNotExpr(self, ctx):
        reg = self.visit(ctx.expr())
        dr = self._current_function.new_tmp()
        # there is no boolean not :-(
        labelneg = self._current_function.new_label("cond_neg")
        labelend = self._current_function.new_label("cond_end")
        self._current_function.addInstructionCondJUMP(labelneg, reg,
                                                      Condition("beq"), 0)
        self._current_function.addInstructionLI(dr, 0)
        self._current_function.addInstructionJUMP(labelend)
        self._current_function.addLabel(labelneg)
        self._current_function.addInstructionLI(dr, 1)
        self._current_function.addLabel(labelend)
        return dr

    def visitUnaryMinusExpr(self, ctx):
        tmp = self.visit(ctx.expr())
        dr = self._current_function.new_tmp()
        self._current_function.addInstructionSUB(dr, Operands.ZERO, tmp)
        return dr

    def visitProgRule(self, ctx):
        self.visitChildren(ctx)
        return

    def visitFuncDecl(self, ctx):
        funcname = ctx.ID().getText()
        self._current_function = RiscVFunction(funcname)
        self._memory = dict()

        self.visit(ctx.vardecl_l())
        self.visit(ctx.block())
        self._current_function.addComment("Return at end of function:")
        # TODO: at some point there will be a non harcoded return value
        # TODO: for functions, but for now, "return 0".
        self._current_function.addInstructionLI(Operands.A0, 0)
        self._functions.append(self._current_function)

        # We don't need to bother with div_by_zero in our CFG, hence remove it
        # if it was added.
        div_0_label = self._current_function.get_label_div_by_zero()
        for jump in div_0_label._in:
            jump._out.remove(div_0_label)
        div_0_label._in = []

        self._current_function = None

    def visitAssignStat(self, ctx):
        if self._debug:
            print("assign statement, rightexpression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        reg4expr = self.visit(ctx.expr())
        name = ctx.ID().getText()
        if name in self._memory:
            self._current_function.addInstructionMV(self._memory[name], reg4expr)
        else:
            raise Exception("Variable is not declared")

    def visitIfStat(self, ctx):
        if self._debug:
            print("if statement")
        # invent a new label, then push in the label stack
        end_if_label = self._current_function.new_label("end_if")
        else_label = self._current_function.new_label('else')
        cond = self.visit(ctx.expr())
        self._current_function.addInstructionCondJUMP(else_label, cond,
                                                      Condition("beq"), 0)
        self.visit(ctx.then_block)
        self._current_function.addInstructionJUMP(end_if_label)
        self._current_function.addLabel(else_label)
        if ctx.else_block is not None:
            if self._debug:
                print("else  ")
            self.visit(ctx.else_block)
        self._current_function.addLabel(end_if_label)


    def visitWhileStat(self, ctx):
        if self._debug:
            print("while statement, condition is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
            print("and block is:")
            print(Trees.toStringTree(ctx.stat_block(), None, self._parser))
        labelbegin = self._current_function.new_label("begin_while")
        labelend = self._current_function.new_label("end_while")
        self._current_function.addLabel(labelbegin)
        reg = self.visit(ctx.expr())
        self._current_function.addInstructionCondJUMP(labelend, reg,
                                                      Condition("beq"), 0)
        self.visit(ctx.stat_block())
        self._current_function.addInstructionJUMP(labelbegin)
        self._current_function.addLabel(labelend)
    # visit statements

    def visitPrintintStat(self, ctx):
        expr_loc = self.visit(ctx.expr())
        if self._debug:
            print("print_int statement, expression is:")
            print(Trees.toStringTree(ctx.expr(), None, self._parser))
        self._current_function.addInstructionPRINTINT(expr_loc)

    def visitPrintfloatStat(self, ctx):
        raise MiniCUnsupportedError("print_float")

    def visitPrintstringStat(self, ctx):
        raise MiniCUnsupportedError("Unsupported type string")

    def visitStatList(self, ctx):
        for stat in ctx.stat():
            self._current_function.addComment(Trees.toStringTree(stat, None, self._parser))
            self.visit(stat)

    def visitForForStat(self, ctx):
        raise NotImplementedError("fortran for")

    def visitArrayAllocExpr(self, ctx):
        raise NotImplementedError("array")

    def visitArrayReadExpr(self, ctx):
        raise NotImplementedError("array")

    def visitArrayWriteStat(self, ctx):
        raise NotImplementedError("array")

    def visitArrayType(self, ctx):
        raise NotImplementedError("array")
