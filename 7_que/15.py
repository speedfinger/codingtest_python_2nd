"""
1,2,3,4,5
2 pop
1,3,4,5

3 pop
1,4,5

"""

from collections import deque

def solution(N, K):
    que = deque(range(1,N+1))
    # print(que)
    while len(que)>1:
        for _ in range(K-1):
            que.append(que.popleft())
        que.popleft()
    return que[0]

print(solution(5,2))