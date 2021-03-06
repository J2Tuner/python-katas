def square_of_sum(n):
    return (1/2 * n * (n + 1))**2
    

def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
