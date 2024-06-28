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


def generate_primes_grid(width, height, start):
    primes = []

    count_nums = width * height
    estimasi_batas_atas = int(
        count_nums**2 * (math.log(count_nums) + math.log(count_nums))
    )
    for i in range(start + 1, estimasi_batas_atas):
        if is_prime(i):
            primes.append(i)
        if len(primes) >= count_nums:
            break

    # print(primes)
    result = ""

    for i in range(0, len(primes), width):
        # print(i)
        slice_primes = primes[i : i + width]
        slice_primes_str = ""
        for _, num in enumerate(slice_primes):
            str_num = str(num)

            if len(str_num) == 1:
                str_num = "  " + str_num
            elif len(str_num) == 2:
                str_num = " " + str_num

            slice_primes_str += str_num

        slice_primes_str = slice_primes_str.strip()
        slice_primes_str += "\n"
        # print(f"--{slice_primes}--")
        result += slice_primes_str

    return result

print(generate_primes_grid(5, 2, 1))

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """
