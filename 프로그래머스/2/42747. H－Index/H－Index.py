def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if c <= i:
            return i
    return len(citations)