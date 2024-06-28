def fibonacci(number):
    if number in [0, 1]:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(1))  # 1
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10))  # 55
    print(fibonacci(12))  # 144
