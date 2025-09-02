def solution(m, n, puddles):
    # m과 n의 순서를 맞춰 2차원 리스트를 생성
    dp = [[0] * m for _ in range(n)]

    # 1. 물웅덩이 위치를 미리 표시
    # 문제의 좌표계 (1,1)을 리스트 인덱스 (0,0)에 맞춤
    for x, y in puddles:
        dp[y - 1][x - 1] = -1  # 물웅덩이 표시

    # 2. DP 테이블 채우기
    for i in range(n):
        for j in range(m):
            # 물웅덩이는 건너뛰기
            if dp[i][j] == -1:
                dp[i][j] = 0  # 경로가 0개
                continue
            
            # 시작점
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            # 위쪽과 왼쪽 경로를 더하여 현재 위치의 경로 개수 계산
            up = dp[i - 1][j] if i > 0 else 0
            left = dp[i][j - 1] if j > 0 else 0

            dp[i][j] = (up + left) % 1000000007

    # 3. 학교 위치의 최단 경로 개수 반환
    return dp[n - 1][m - 1]