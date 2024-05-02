def print_natural_numbers(n):
    if n < 1:
        return
    print_natural_numbers(n - 1)
    print(n)
