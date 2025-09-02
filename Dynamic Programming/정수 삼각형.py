def solution(triangle):
    # dp 테이블을 삼각형과 동일한 크기로 초기화 (깊은 복사)
    dp = [row[:] for row in triangle]

    # 두 번째 줄부터 마지막 줄까지 순차적으로 계산
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 맨 왼쪽 칸
            if j == 0:
                dp[i][j] += dp[i-1][j]
            # 맨 오른쪽 칸
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            # 중간 칸
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

    # 마지막 줄에서 최댓값 반환
    return max(dp[-1])