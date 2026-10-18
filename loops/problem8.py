  # Prime Numbers

number = 7

is_prime = True

if number >1:
    for i in range(2, number+1):
        if (number % i) == 0:
            is_prime = False
            break