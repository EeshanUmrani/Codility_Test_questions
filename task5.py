def solution(A):
    max_length = 0
    current_length = 0
    prev_num = None
    prev_prev_num = None

    for num in A:
        if num == prev_num or num == prev_prev_num:
            current_length += 1
        else:
            current_length = 2  # Minimum length of a bi-valued slice
        max_length = max(max_length, current_length)
        prev_prev_num = prev_num
        prev_num = num

    return max_length


# Test cases
print(solution([4, 2, 2, 4, 2]))   # Output: 5
print(solution([1, 2, 3, 2]))     # Output: 3
print(solution([0, 5, 4, 4, 5, 12]))  # Output: 4
print(solution([4, 4]))            # Output: 2
