def solution(N, number):
    # dp[i] = N을 i+1번 사용해서 만들 수 있는 모든 수의 집합
    dp = [set([int(str(N)*(i+1))]) for i in range(8)]
    
    for i in range(8):
        for j in range(i):
            # dp[j]: N을 (j+1)번 사용
            # dp[i-j-1]: N을 (i-j)번 사용
            for num1 in dp[j]:
                for num2 in dp[i-j-1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        # 매번 number가 나왔는지 확인
        if number in dp[i]:
            return i + 1  # i는 0부터 시작하므로 +1
    return -1

            