# def solution(people, limit):
#     answer = 0
#     while len(people) > 1:
#         for i in people:
#             c = people.pop(0)
#             if c+i <= limit:
#                 people.remove(i)
#                 answer+=1
#             else:
#                 answer+=1
#     return answer

def solution(people, limit):
    people.sort()  # 가장 가벼운 사람부터 정렬
    left = 0
    right = len(people) - 1
    answer = 0

    while left <= right:
        if people[left]+people[right] <= limit:
            left+=1
        right-=1
        answer+=1

    return answer

