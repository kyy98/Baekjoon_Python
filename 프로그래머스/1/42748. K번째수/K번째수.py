commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1,5,2,6,3,7,4]

def solution(array, commands):
    ls = []
    for a in commands:
        arr1 = array[a[0]-1:a[1]]
        arr1 = sorted(arr1)
        b = arr1[a[2]-1]
        ls.append(b)
    return ls
solution(array, commands)
    