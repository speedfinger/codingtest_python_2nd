"""
https://school.programmers.co.kr/learn/courses/30/lessons/131127

["banana", "apple", "rice", "pork", "pot"]	[3, 2, 2, 2, 1]	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	3
["apple"]	[10]	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]	0


 행사 끝나면 다시 0번으로 돌아가지 않는 점을 주의


"""

from collections import defaultdict
from copy import deepcopy
from pprint import pprint



def solution(want, number, discount):
    # print(want)
    data = defaultdict(int)
    datas = []
    
    target= defaultdict(int)
    for idx,item in enumerate(want):
        target[item]=number[idx]
    
    # pprint(target)
    match_count = 0
    for idx,item in enumerate(discount[0:10]):
        # print(item)
        # print((item))
        tmp = data[(item)]
        data[(item)] = tmp+1
        if target==data:
            match_count+=1
        
    datas.append(data)
    # print(discount[0:10])

        # tmp = data["0"][item]
        # data["0"][item] = tmp+1
    # data["0"]=
    
    for idx in range(1,len(discount)-9):
        # print(f"idx:{idx}: {discount[idx:10+idx]}")
        tmp_dict = deepcopy(data)
        # print(tmp_dict)
        remove_item=discount[idx-1]
        new_item=discount[idx+9]
        # print(f"{remove_item}/{new_item}")
        tmp_dict[remove_item]=tmp_dict[remove_item]-1
        
        if tmp_dict[remove_item] == 0:
            del tmp_dict[remove_item]
            
        tmp_dict[new_item]=tmp_dict[new_item]+1
        # datas.append(tmp_dict)
        if target==tmp_dict:
            match_count+=1
        
        data = tmp_dict
   
    # pprint(datas)
    return match_count
  
# print(solution(["banana", "apple", "rice", "pork", "pot"],	[3, 2, 2, 2, 1]	
#                ,["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
# print(solution(["apple"],	[10],	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
# print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana", "chicken", "apple"]))


"""
1]21_best 와 비교했을때 성능상 이점이 있을까?

모범답안은 10*len(discount)
내 풀이는 len(discount) ??

2] from collections import Counter
의 활용!!
"""