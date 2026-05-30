def differ_by_insertion(str1, str2):

    str1 = str1.split(" ")
    str2 = str2.split(" ")

    if len(str1) > len(str2):
        str2 , str1 = str1, str2

    n = len(str1)

    i = 0

    while i < n and str1[i] == str2[i]:
        i+=1

    j = 0

    while j < n - i and str1[-1-j] == str2[-1-j]:
        j+=1

    return i + j == len(str1)


print(differ_by_insertion("a b", "a b"))
