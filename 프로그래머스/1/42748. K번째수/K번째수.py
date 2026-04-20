def solution(array, commands):
    ans = []
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        array_2 = array[i-1:j]
        array_2.sort()
        ans.append(array_2[k-1])
    return ans