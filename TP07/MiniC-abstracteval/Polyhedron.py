from linpy import Symbol, Dummy, Polyhedron, Empty, Universe
from math import ceil, floor, inf

# Function for polyhedrons

def poly_empty():
    """
    Returns the Empty polyhedron
    """
    return Empty

def poly_is_empty(p):
    """
    Return True if the polyhedron is empty
    """
    return p.isempty()

def poly_universe():
    """
    Returns the "all universe" polyhedron
    """
    return Universe

def poly_is_universe(p):
    """
    Return True if the polyhedron is the "all universe" polyhedron
    """
    return p.isuniverse()

def poly_union(p1, p2):
    """
    Compute and returns the convex hull of the union
    """
    return Polyhedron(p1 | p2)

def poly_inter(p1, p2):
    """
    Compute and returns the intersection
    """
    return Polyhedron(p1 & p2)

def poly_compl(p):
    """
    Compute and returns the convex hull of the complement.
    Should not be useful.
    """
    return Polyhedron(Universe - p)


def poly_widen(p1, p2):
    """
    Widening of the first polyhedron by the second polyhedron
    """
    assert(isinstance(p1,Polyhedron))
    assert(isinstance(p2,Polyhedron))
    return p1.widen(p2)

def poly_incl(p1, p2):
    """
    True if p1 is included in p2
    """
    return p1 <= p2

# Functions handling variable name in polyhedron
# Variable names must be str starting by a letter or _, 
# and containing only letters, numbers or _

def poly_vars(poly):
    """
    Return the set of all variables constrained by the polyhedron
    (unconstrained variables are not returned)
    """
    s = set()
    for symbol in poly.symbols:
       s.add(str(symbol))
    return s

def poly_forget(poly, name):
    """
    Project out the variable from the poly description
    (we forget any information we knew about the variable name)
    """
    p = poly.project([Symbol(name)])
    return p

def poly_subs(poly, oldname, newname):
    """
    Var substitution
    """
    return poly.subs(Symbol(oldname), Symbol(newname))

def poly_to_interval(poly,name):
    """
    Project out every variable but name, then return (vmin,vmax)
    where vmin is the minimal value for name (or -math.inf, if unbounded)
    and vmax is the maximal value for name (or math.inf, if unbounded)
    It returns (1,-1) for the empty interval, and (-math.inf,math.inf) for the full interval.
    """
    if poly_is_empty(poly):
       return 1,-1
    p = poly
    symbol = Symbol(name)
    for var in poly.symbols:
        if var != symbol:
           p = p.project([var])
    # Now, we should either have "name == N" or "N1 <= name <= N2"
    eq = p.equalities
    eq_min = None
    eq_max = None
    if len(eq) > 1:
       raise Exception # Too many equalities. Projecting didn't work?
    elif len(eq) == 1:
       eq_min = eq[0]
       eq_max = eq[0]
    else:
       ineq = p.inequalities
       for i in ineq:
          if i.coefficient(symbol) > 0:
             if eq_min is not None:
                 raise Exception # Too many lower bounds. Projecting didn't work?
             else:
                 eq_min = i
          elif i.coefficient(symbol) < 0:
             if eq_max is not None:
                 raise Exception # Too many upper bounds. Projecting didn't work?
             else:
                 eq_max = i
          else:
                 raise Exception # Unrelated inequality. Projecting didn't work?
    # Now, both eq_min and eq_max contain the lower and upper bound under the form of an equality, or None 
    val_min = -inf if eq_min is None else int(ceil(- eq_min.constant / eq_min.coefficient(symbol)))
    val_max = inf if eq_max is None else int(floor(- eq_max.constant / eq_max.coefficient(symbol)))
    # We make sure to round correctly, since we know all values are integers
    return val_min,val_max
      

# Functions handling linear expressions

def to_lin_expr(name_or_int):
    """
    Returns the linear expression corresponding to name_or_int
    which can be either a name (str) or an integer (int)
    """
    return Symbol(name_or_int) if isinstance(name_or_int,str) else name_or_int
    
# You can make affine combinations of linear expression, for example:
# l1 = to_lin_expr(var1)
# l2 = to_lin_expr(var2)
# l3 = to_lin_expr(42)
# l4 = -l1+3*l2-10*l3+18

def poly_eqz(linexpr):
    """
    Returns the polyhedron corresponding to "linexpr == 0"
    """
    return Polyhedron([linexpr],[])

def poly_geqz(linexpr):
    """
    Returns the polyhedron corresponding to "linexpr >= 0"
    """
    return Polyhedron([],[linexpr])

    
