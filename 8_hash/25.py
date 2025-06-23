""" 
https://school.programmers.co.kr/learn/courses/30/lessons/72411
"ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]
"""


from itertools import combinations
from collections import defaultdict, Counter
from pprint import pprint

def make_cobinations(input:str,course:list)->list:
    result = set()

    for r in course:
        for comb in combinations(input, r):
            sorted_str = ''.join(sorted(comb))
            result.add(sorted_str)
    # print(len(result))
    return result

def retry_make_conbinations(input,r)->list:
    result = set()
    for comb in combinations(input, r):
        sorted_str = ''.join(sorted(comb))
        result.add(sorted_str)
    return result

menu_count =  defaultdict(int)
courses= [defaultdict(int) for _ in range(10)]


def solution(orders, course):
    answer = []
    # print(make_cobinations(orders[0]))
    
    for order in orders:
        #old
        # order_combinations = make_cobinations(order,course)
        # print(f"order:{order} \n{order_combinations}")
        # for combination in order_combinations:
        #     # print(combination)
        #     length = len(combination)
        #     menu_dict = courses[length]
        #     menu_dict[combination]=menu_dict[combination]+1
        for r in course:
            order_combinations = retry_make_conbinations(order,r)
            for combination in order_combinations:
                menu_dict = courses[r]
                menu_dict[combination]=menu_dict[combination]+1
            
    
    # pprint(courses)
    # print()
    
    
    
    for cnt in course:
        # print(courses[cnt])
        # print()
        
        course = courses[cnt]
        # pprint(course)
        if len(course)>=1:
            max_value = max(course.values())

        if max_value<2:
            continue
        result = [k for k, v in course.items() if v == max_value]
        # print(result)
        for _ in result:
            answer.append(_)
    
    
    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]	))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"]	,[2,3,4]))


""" 
1. make_cobinations
부분을 2부터 len(input)  까지 만들지 않고 
course 길이까지만 만들도록 변경




"""