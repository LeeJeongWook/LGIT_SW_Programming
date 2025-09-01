import heapq

def solution(scoville, K):
    answer = 0
    min_heap = []
    
    for s in scoville:
        heapq.heappush(min_heap, s)

    while min_heap:
        if all(item >= K for item in min_heap):
            break

        if len(min_heap) < 2:
            return -1
        
        min_scov1 = heapq.heappop(min_heap)
        min_scov2 = heapq.heappop(min_heap)
        new_scoville = min_scov1 + (min_scov2 * 2)
        heapq.heappush(min_heap, new_scoville)

        answer += 1

    return answer