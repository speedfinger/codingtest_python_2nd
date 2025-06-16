"""
https://school.programmers.co.kr/learn/courses/30/lessons/159994
"""
from collections import deque
def solution(cards1, cards2, goal):
    
    card_1=deque(cards1)
    card_2=deque(cards2)
    for word in goal:
        if len(card_1)!=0 and card_1[0]==word:
            card_1.popleft()
        elif len(card_2)!=0 and card_2[0]==word:
            card_2.popleft()
        else:
            return "No"
    return "Yes"


# print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
# print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"])  )