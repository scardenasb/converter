import math as mt


# TODO: Looking how to use exponents as
# conversion factors (try to find the most accurate Logarithm's with base 10)
def unit_calculator(value, from_exp, to_exp):

    exp = to_exp - from_exp
    to_unit = round(value * 10 ** exp, 5)

    return to_unit
