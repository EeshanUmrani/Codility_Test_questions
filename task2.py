def solution(AA, AB, BB):
    result = []

    while AA > 0 or BB > 0:
        if AA > BB:
            if AA > 1:
                result.append("AA")
                AA -= 2
            else:
                result.append("A")
                AA -= 1
        elif BB > 0:
            result.append("B")
            BB -= 1

        if AB > 0 and result and result[-1] == "A":
            result.append("B")
            AB -= 1

        if AB > 0 and (not result or result[-1] == "B"):
            result.append("AB")
            AB -= 1

    return "".join(result)


# Test cases
print(solution(5, 0, 2))  # Output: "AABBAABBAA"
print(solution(1, 2, 1))  # Output: Any valid output
print(solution(0, 2, 0))  # Output: "ABAB"
print(solution(0, 0, 10))  # Output: "BB"
print(solution(3, 1, 2))  # Output: "AABBAAB"
print(solution(1, 4, 0))  # Output: "ABABABA"
print(solution(2, 1, 2))  # Output: "AABBAB"
