import heapq

def solution(jobs):
    # 1. 작업을 요청 시각 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    total_jobs = len(jobs)
    current_time = 0
    total_turnaround_time = 0
    job_index = 0
    wait_queue = []
    
    while job_index < total_jobs or wait_queue:
        # 2. 현재 시점에 요청된 모든 작업을 힙에 추가
        while job_index < total_jobs and jobs[job_index][0] <= current_time:
            # heapq는 최소 힙을 구현. (소요 시간, 요청 시간) 순서로 튜플을 힙에 넣음
            heapq.heappush(wait_queue, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
            
        # 3. 힙에 작업이 있다면 가장 짧은 작업을 처리
        if wait_queue:
            duration, request_time = heapq.heappop(wait_queue)
            
            # 작업 시작 시점은 현재 시점
            start_time = current_time
            # 작업 완료 시점 업데이트
            current_time += duration
            
            # 반환 시간 = (완료 시점 - 요청 시점)
            turnaround_time = current_time - request_time
            total_turnaround_time += turnaround_time
        
        # 4. 힙이 비어있고, 아직 처리할 작업이 남았다면 다음 작업 요청 시점으로 시간 점프
        else:
            if job_index < total_jobs:
                current_time = jobs[job_index][0]

    # 5. 평균 반환 시간 계산 (정수 부분만 반환)
    return total_turnaround_time // total_jobs