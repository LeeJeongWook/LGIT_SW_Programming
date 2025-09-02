from collections import Counter

def solution(clothes):
    answer = 1
    
    clothes = dict(clothes)
    count = Counter(clothes.values())
    
    for i in count.values():
        answer *= i + 1
    answer -= 1
    return answer