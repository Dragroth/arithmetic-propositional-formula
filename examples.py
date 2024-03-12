### Single argument

test_formula = (
        "p"
    )
test_variables = ('p')

### Two arguments

test_formula = (
        "NOT", "p"
    )
test_variables = ('p')

### Three arguments

test_formula = (
        'p', 'IMPLIES', 'p'
    )
test_variables = ('p', 'q')

### Three arguments (recursive)

test_formula = (
        'p', 'IMPLIES', ('NOT', 'q')
    )
test_variables = ('p', 'q')

### Three arguments (recursive)

test_formula = (
        ('p', 'IMPLIES', ('NOT', 'q')),
        'OR',
        ('p', 'AND', 'q')
    )
test_variables = ('p', 'q')
