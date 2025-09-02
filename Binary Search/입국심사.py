def solution(n, times):
    # 이진 탐색의 탐색 범위 설정
    start = 1  # 최소 시간은 1분부터 시작
    end = max(times) * n # 최대 시간: 가장 오래 걸리는 심사관이 모든 사람을 처리하는 경우
    answer = end # 최소 시간을 저장할 변수, 초기값은 최대 시간으로 설정

    while start <= end:
        mid = (start + end) // 2
        
        # mid 시간 동안 처리할 수 있는 총 사람 수 계산
        total_people = 0
        for time in times:
            total_people += mid // time

        if total_people >= n:
            # mid 시간 내에 모든 사람을 처리할 수 있는 경우
            # 더 짧은 시간으로도 가능한지 탐색하기 위해 end를 줄임
            answer = mid
            end = mid - 1
        else:
            # mid 시간 내에 모든 사람을 처리할 수 없는 경우
            # 시간을 더 늘려야 하므로 start를 늘림
            start = mid + 1
            
    return answer