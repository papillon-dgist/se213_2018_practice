def divide(dividend, divisor):
    """Return (quotient, remainder)"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder # return a tuple

q, r = divide(13,3) # tuple unpacking
print('quotient = ', q, ', remainder = ', r, sep='')