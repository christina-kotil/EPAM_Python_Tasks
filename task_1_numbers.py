import math
def func_1 (a,b):
    value = (12 * a + 25 * b) / (1 + a ** (2 ** b))
    return math.ceil(value * 100) / 100
