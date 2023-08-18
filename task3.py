def solution(S):
    lines = S.strip().split('\n')
    min_name_length = float('inf')

    for line in lines:
        owner, perm, name = line.split()
        extension = name.split('.')[-1]

        if extension in ["doc", "xls", "pdf"] and \
                perm[0] == 'r' and perm[1] == '-' and perm[2] != 'w' and \
                owner == "root":
            min_name_length = min(min_name_length, len(name))

    if min_name_length == float('inf'):
        return "NO FILES"
    else:
        return str(min_name_length)


