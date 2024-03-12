test_formula = (
        "p"
    )
test_variables = ('p')

###

test_formula = (
        ("NOT", "p")
    )
test_variables = ('p')

###

test_formula = (
        ('p', 'IMPLIES', ('NOT', 'q'))
    )
test_variables = ('p', 'q')

###

test_formula = (
        ('p', 'IMPLIES', ('NOT', 'q')),
        'OR',
        ('p', 'AND', 'q')
    )
test_variables = ('p', 'q')
