"""
https://school.programmers.co.kr/learn/courses/30/lessons/159994
"""
from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    
    card_1=deque(cards1)
    card_2=deque(cards2)
    goal_ = deque(goal)
    
    word_1=None
    word_2=None
    context = None
    
    while True:
        if len(goal_)==0:
            break
        
        if word_1 is None and len(card_1)!=0:
            word_1 = card_1.popleft()
        if word_2 is None and len(card_2)!=0:
            word_2 = card_2.popleft()
        
        if context is None and len(goal_)!=0:
            context = goal_.popleft()
            
            
        if context == word_1:
            
            if word_1 is None:
                word_1=-1
                continue
            
            context = None
            word_1 = None
            
        if context == word_2:
            if word_2 is None:
                word_2=-1
                continue
            context = None
            word_2 = None
            
        if context is not None:
            # 이 코드를 안넣으면 TC에서 1개가 오답처리 됨
            goal_.append("dummy")
            break
    
    return "Yes" if len(goal_)==0 else "No"


# print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
# print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"])  )