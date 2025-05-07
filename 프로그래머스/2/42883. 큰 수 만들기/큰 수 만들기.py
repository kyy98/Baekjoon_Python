## 맨 앞자리수가 클수록 숫자는 커진다는 점을 이용
## 스택을 이용해서 맨 앞자리부터 순차적으로 수를 하나씩 검사하며, 
## 앞자리 수를 가능한 크게 만드는 선에서 k개의 숫자를 제외
def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and k > 0 and num > stack[-1]:
            stack.pop()
            k-=1
        stack.append(num)
    if k:
        return number[:k+1]
    else:
        return ''.join(i for i in stack)
        

    
    

        
            
            
    
                