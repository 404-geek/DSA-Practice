def differ_by_insertion(str1, str2):

    str1 = str1.split(" ")
    str2 = str2.split(" ")

    l = len(str1)
    m = len(str2)
    sm = max(l,m)
    sh = min(l,m)

    for i in range(sm):

        if str1[i] != str2[i]:
            break
    
    for j in range(1, sm):
        if str1[-j] != str2[-j]:
            break

    if len(str1[:i]) + len(str1[i:j]) == sh:
        return True
    else:
        return False


print(differ_by_insertion("a b", "a b"))
