"""
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
from collections import deque

def get_how_long_take(progress,speed):
    day = 0
    while True:
        if progress>=100:
            break
        progress=progress+speed
        day=day+1
    return day

def solution(progresses,speeds):
    answer = []
    que = deque()
    # print(progresses)
    # print(speeds)
    for i in range(0,len(progresses)):
        print(f"progress:{progresses[i]} / {speeds[i]}")
        progresse_i = progresses[i]
        speed_i = speeds[i]
        day=get_how_long_take(progresse_i,speed_i)
        # print(day)
        que.append(day)
    # print(que)
    
    max = que.popleft()
    cnt = 1
    while len(que)>0:
        tmp=que.popleft()
        # print(f"tmp:{tmp} / max:{max}")

        # if len(que)==0:
        #     answer.append(cnt)
        
        if max<tmp:
            answer.append(cnt)
            max=tmp
            cnt=1

        else:
            cnt=cnt+1
    answer.append(cnt)
    # print(answer)
    # print(cnt)

        
        
        

    return answer

solution([93,30,55],[1,30,5])    
# solution([95,90,99,99,80,99],[1,1,1,1,1,1])