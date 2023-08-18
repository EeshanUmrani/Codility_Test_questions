def solution(A):
    if len(A) < 2:
        return len(A)

    A.sort()

    max_count = 1
    for i in range(len(A) - 1):
        count = 1
        diff = A[i + 1] - A[i]

        while i + count < len(A) and A[i + count] - A[i + count - 1] == diff:
            count += 1
            max_count = max(max_count, count)

    return max_count


# Test cases
print(solution([12, 12, 12, 15, 10]))  # Output: 3
print(solution([18, 26, 18, 24, 24, 20, 22]))  # Output: 4
print(solution([4, 4, 4, 4]))  # Output: 4
print(solution([1, 2, 3, 4, 5]))  # Output: 5
print(solution([1, 3, 5, 7, 9]))  # Output: 5
print(solution([4, 3, 1, 5, 4, 4]))  # Output: 3
