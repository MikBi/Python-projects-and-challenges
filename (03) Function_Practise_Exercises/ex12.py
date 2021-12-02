def count_primes(num):
    # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    counter = 0
    for n in range(2, (num + 1)):
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            counter += 1
    return counter


print(count_primes(100))
