# Write code for algorithm 4 below
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
