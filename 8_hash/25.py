""" 
https://school.programmers.co.kr/learn/courses/30/lessons/72411
"ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]
"""


from itertools import combinations
from collections import defaultdict
# s = "ABCFG"
def make_cobinations(input:str)->list:
    result = set()

    for r in range(2, len(input)+1):
        for comb in combinations(input, r):
            sorted_str = ''.join(sorted(comb))
            result.add(sorted_str)

    # 결과를 정렬해서 출력
    # for item in sorted(result):
    #     print(item)
    return result

menu_count =  defaultdict(int)

def solution(orders, course):
    answer = []
    # print(make_cobinations(orders[0]))
    
    for order in orders:
        order_combinations = make_cobinations(order)
        # print(f"order:{order} \n{order_combinations}")
        
        for combination in order_combinations:
            # print(combination)
            menu_count[combination]=menu_count[combination]+1
    
    print(menu_count)
    
    set_menu_dict = defaultdict(list)
    for number in course:
        set_menu_dict[number]=[]
    
    for menu in menu_count:
        # print(f"menu:{menu} : {menu_count[menu]}")
        cnt = menu_count[menu]
        if set_menu_dict.get(cnt) is not None:
            set_menu_dict[cnt].append(menu)
    print(set_menu_dict)
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]	))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"]	,[2,3,4]))