# def solution(n):
#     def fibo(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return fibo(n-1)+fibo(n-2)
#     return (fibo(n-1)+fibo(n-2))%1234567
    

def solution(n):
    answer = [0,1]
    for i in range(2, n+1):
        answer.append((answer[i-1]+answer[i-2]) % 1234567)
    return answer[-1]
    
    