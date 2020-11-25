# Generated from MiniC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#progRule.
    def visitProgRule(self, ctx:MiniCParser.ProgRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#funcDeclEmpty.
    def visitFuncDeclEmpty(self, ctx:MiniCParser.FuncDeclEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#varDeclList.
    def visitVarDeclList(self, ctx:MiniCParser.VarDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#varDecl.
    def visitVarDecl(self, ctx:MiniCParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#paramDecl.
    def visitParamDecl(self, ctx:MiniCParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#paramListBase.
    def visitParamListBase(self, ctx:MiniCParser.ParamListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#paramList.
    def visitParamList(self, ctx:MiniCParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#paramListEmpty.
    def visitParamListEmpty(self, ctx:MiniCParser.ParamListEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#idListBase.
    def visitIdListBase(self, ctx:MiniCParser.IdListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#idList.
    def visitIdList(self, ctx:MiniCParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statList.
    def visitStatList(self, ctx:MiniCParser.StatListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#stat.
    def visitStat(self, ctx:MiniCParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignStat.
    def visitAssignStat(self, ctx:MiniCParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ifStat.
    def visitIfStat(self, ctx:MiniCParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#condBlock.
    def visitCondBlock(self, ctx:MiniCParser.CondBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#stat_block.
    def visitStat_block(self, ctx:MiniCParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#whileStat.
    def visitWhileStat(self, ctx:MiniCParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#forForStat.
    def visitForForStat(self, ctx:MiniCParser.ForForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#cpt.
    def visitCpt(self, ctx:MiniCParser.CptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#arrayWriteStat.
    def visitArrayWriteStat(self, ctx:MiniCParser.ArrayWriteStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assertStat.
    def visitAssertStat(self, ctx:MiniCParser.AssertStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printintStat.
    def visitPrintintStat(self, ctx:MiniCParser.PrintintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printfloatStat.
    def visitPrintfloatStat(self, ctx:MiniCParser.PrintfloatStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printstringStat.
    def visitPrintstringStat(self, ctx:MiniCParser.PrintstringStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exprListEmpty.
    def visitExprListEmpty(self, ctx:MiniCParser.ExprListEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exprListBase.
    def visitExprListBase(self, ctx:MiniCParser.ExprListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#exprList.
    def visitExprList(self, ctx:MiniCParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#notExpr.
    def visitNotExpr(self, ctx:MiniCParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#randExpr.
    def visitRandExpr(self, ctx:MiniCParser.RandExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MiniCParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#arrayReadExpr.
    def visitArrayReadExpr(self, ctx:MiniCParser.ArrayReadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#atomExpr.
    def visitAtomExpr(self, ctx:MiniCParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#orExpr.
    def visitOrExpr(self, ctx:MiniCParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#funcCall.
    def visitFuncCall(self, ctx:MiniCParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#arrayAllocExpr.
    def visitArrayAllocExpr(self, ctx:MiniCParser.ArrayAllocExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:MiniCParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#relationalExpr.
    def visitRelationalExpr(self, ctx:MiniCParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MiniCParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#andExpr.
    def visitAndExpr(self, ctx:MiniCParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parExpr.
    def visitParExpr(self, ctx:MiniCParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#numberAtom.
    def visitNumberAtom(self, ctx:MiniCParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#booleanAtom.
    def visitBooleanAtom(self, ctx:MiniCParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#idAtom.
    def visitIdAtom(self, ctx:MiniCParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#stringAtom.
    def visitStringAtom(self, ctx:MiniCParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#basicType.
    def visitBasicType(self, ctx:MiniCParser.BasicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#arrayType.
    def visitArrayType(self, ctx:MiniCParser.ArrayTypeContext):
        return self.visitChildren(ctx)



del MiniCParser