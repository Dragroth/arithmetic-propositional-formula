def eval_formula(formula: str, values: dict):
    """
    Evaluate the propositional formula using arithmetic method.
    formula: The propositional formula in structured format (tuple/list) with infix notation.
    values: A dictionary of truth values for each variable in the formula, including TRUE and FALSE.
    """
    # Update values dictionary to include TRUE and FALSE
    values.update({"TRUE": 1, "FALSE": 0})

    # Define logical operators as functions
    def NOT(x):
        return 1 - x
    
    def AND(x, y):
        return x * y
    
    def OR(x, y):
        return x + y - x * y
    
    def IMPLIES(x, y):
        return 1 - x + x * y

    # Evaluate the formula recursively
    if type(formula) == str: # Base case: variable, e.g. formula = 'p'
        return values[formula]  
    if len(formula) == 2:  # Unary operator case, e.g. formula = ('NOT', 'p')
        op, arg = formula
        return eval(op.upper())(eval_formula(arg, values))
    # Binary operator case, e.g. formula = ('p', 'OR', 'q')
    left, op, right = formula
    return eval(op.upper())(eval_formula(left, values), eval_formula(right, values))

def is_tautology(formula: str, variables: tuple):
    """
    Check if the given propositional formula is a tautology.
    formula: The propositional formula in structured format.
    variables: A tuple of variables in the formula.
    """
    # Loop 2**n times where n is number of variables in formula (e.g. 8 times for p, q and r)
    for bits in range(2**len(variables)):
        # Map every bits value to different variables, (e.g. when bits = 0: values[p] = 0, values[q] = 0; bits = 1: values[p] = 1, values[q] = 0)
        values = {var: (bits >> i) & 1 for i, var in enumerate(variables)}
        if not eval_formula(formula, values):
            # Found a case where the formula is not true
            print(values)
            return False
    # The formula is true for all possible values 
    return True

if __name__ == "__main__":
    # The tested formula
    # The formula should be a string or a tuple/list of strings
    # Note that the function works recursively and it only works with 1 (variable), 2 (NOT) or 3 arguments (binary operators), for example ((p OR q) OR r) is supported but (p OR q OR r) is not
    test_formula = (
        ('p', 'IMPLIES', ('NOT', 'q')),
        'OR',
        ('p', 'AND', 'q')
    )

    # Remember to always set test variables used in test formula
    test_variables = ('p', 'q')

    if is_tautology(test_formula, test_variables):
        print("The test formula is a tautology.")
    else:
        print("The test formula is not a tautology.")
