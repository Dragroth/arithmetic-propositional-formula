# arithmetic-propositional-formula

This simple script can be used to check whether a given propositional formula is a tautology. It uses arithmetic method and works recursively.

## Usage
1. Change the test formula variable to your own formula.
2. Set test variables
3. Run the script: `python propositional-formula.py`

## Notes
The formula should be a string or a tuple/list of strings.
The function works recursively and it only works with 1 (variable), 2 (NOT) or 3 arguments (binary operators), for example ((p OR q) OR r) is supported but (p OR q OR r) is not. Check examples in the script for reference.
