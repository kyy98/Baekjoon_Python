def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == s1[i%len(s1)]:
            cnt_1+=1
        if answers[i] == s2[i%len(s2)]:
            cnt_2+=1
        if answers[i] == s3[i%len(s3)]:
            cnt_3+=1
    ans_1 = [cnt_1,cnt_2,cnt_3]
    ans_1.sort(reverse=True)
    ans = []
    ans_2 = [(1,cnt_1), (2,cnt_2), (3,cnt_3)]
    for a in ans_2:
        if a[1] == ans_1[0]:
            ans.append(a[0])
    return ans