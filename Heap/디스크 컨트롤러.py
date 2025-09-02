import heapq

def solution(jobs):
    # 1. �۾��� ��û �ð� �������� ����
    jobs.sort(key=lambda x: x[0])
    
    total_jobs = len(jobs)
    current_time = 0
    total_turnaround_time = 0
    job_index = 0
    wait_queue = []
    
    while job_index < total_jobs or wait_queue:
        # 2. ���� ������ ��û�� ��� �۾��� ���� �߰�
        while job_index < total_jobs and jobs[job_index][0] <= current_time:
            # heapq�� �ּ� ���� ����. (�ҿ� �ð�, ��û �ð�) ������ Ʃ���� ���� ����
            heapq.heappush(wait_queue, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
            
        # 3. ���� �۾��� �ִٸ� ���� ª�� �۾��� ó��
        if wait_queue:
            duration, request_time = heapq.heappop(wait_queue)
            
            # �۾� ���� ������ ���� ����
            start_time = current_time
            # �۾� �Ϸ� ���� ������Ʈ
            current_time += duration
            
            # ��ȯ �ð� = (�Ϸ� ���� - ��û ����)
            turnaround_time = current_time - request_time
            total_turnaround_time += turnaround_time
        
        # 4. ���� ����ְ�, ���� ó���� �۾��� ���Ҵٸ� ���� �۾� ��û �������� �ð� ����
        else:
            if job_index < total_jobs:
                current_time = jobs[job_index][0]

    # 5. ��� ��ȯ �ð� ��� (���� �κи� ��ȯ)
    return total_turnaround_time // total_jobs