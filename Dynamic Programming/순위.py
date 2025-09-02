def solution(n, results):
    # 1. 그래프 초기화
    # 승패 관계를 저장할 2차원 배열 (n+1 x n+1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    # 직접적인 승패 관계를 그래프에 반영
    for winner, loser in results:
        graph[winner][loser] = True
        
    # 2. 플로이드-워셜 알고리즘 적용
    # k: 경유 노드, i: 시작 노드, j: 도착 노드
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # i가 k를 이기고 k가 j를 이겼다면, i는 j를 이긴다
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
                    
    # 3. 순위 확정 선수 수 계산
    answer = 0
    for i in range(1, n + 1):
        win_count = 0
        lose_count = 0
        # i가 이긴 선수 수 세기
        for j in range(1, n + 1):
            if graph[i][j]:
                win_count += 1
        # i에게 진 선수 수 세기 (j가 i를 이겼는지 확인)
        for j in range(1, n + 1):
            if graph[j][i]:
                lose_count += 1
        
        # 순위가 확정된 선수인지 확인 (이긴 선수 + 진 선수 = n - 1)
        if win_count + lose_count == n - 1:
            answer += 1
            
    return answer