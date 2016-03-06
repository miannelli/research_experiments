code = """
def f(x):
    x = x + 1
    return x

print 'This is my output.' + str(f(6))
"""

exec code