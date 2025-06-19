"""
https://school.programmers.co.kr/learn/courses/30/lessons/131127

python
from collections import Counter

collections 모듈과 Counter란?
collections는 파이썬 표준 라이브러리 중 하나로, 여러 가지 유용한 자료구조를 제공합니다.

그 중 Counter는 "데이터의 개수를 세는 데" 특화된 자료구조(클래스)입니다.

Counter는 리스트, 튜플, 문자열 등 반복 가능한(iterable) 객체에서 각 요소가 몇 번 나오는지 세어주는 딕셔너리 형태의 객체입니다.

lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
cnt = Counter(lst)
print(cnt)
출력:

text
Counter({'apple': 3, 'banana': 2, 'orange': 1})

"""
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer