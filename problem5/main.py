def max_sequence(arr):
    max_result = arr[0]
    max_current = max_result

    for num in arr[1:]:
        max_current = max(num, max_current + num)

        if max_result < max_current:
            max_result = max_current

    return max_result


if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))  # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))  # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))  # 12
    print(max_sequence([12, -5, 6, 2, -3, 1, 6, -6]))  # 12
