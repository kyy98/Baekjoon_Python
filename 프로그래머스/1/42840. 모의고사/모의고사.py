def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    ls = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == s1[i%(len(s1))]:
            ls[0]+=1
        if answers[i] == s2[i%(len(s2))]:
            ls[1]+=1
        if answers[i] == s3[i%(len(s3))]:
            ls[2]+=1
    ls_2 = []
    for num in enumerate(ls):
        if num[1] == max(ls):
            ls_2.append(num[0]+1)
    return ls_2
    
