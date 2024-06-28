import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primeX(x):
    if x == 1:
        return 2
    if x == 2:
        return 3

    prime = 0
    count = 2
    estimasi_batas_atas = int(x**2 * (math.log(x) + math.log(x)))
    for i in range(5, estimasi_batas_atas, 2):
        if is_prime(i):
            prime = i
            count += 1

        if count >= x:
            break

    return prime


if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10))  # 29
    print(primeX(20))  # 29
