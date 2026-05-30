

def max_ramp(s):

    occ = {}
    n = len(s)
    max_r = 0

    for ind, i in enumerate(s):
        if not i in occ:
            occ[i] = ind

    for j in range(n-1, -1, -1):

        ch = s[j]

        for c in range(ord('a'), ord(ch)):

            sm = chr(c)

            if sm in occ:
                max_r = max(max_r, j - occ[sm] + 1)

    return max_r

print(max_ramp(s="dbabcb"))