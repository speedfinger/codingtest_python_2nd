"""
https://school.programmers.co.kr/learn/courses/30/lessons/92334

["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]
"""

from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    
    user_report_dict = defaultdict(dict)
    reported_count_dict = defaultdict(int)
    
    for idx, item in enumerate(report):
        user , reported = item.split(" ")
        
        # print(f"user:{user} report: {reported}")
        
        # print(user_report_dict[user])
        
        user_reports = user_report_dict[user].get(reported)
        # print(user_reports)
        if user_reports is None:
            user_report_dict[user][reported]="1"
            
            reported_count_dict[reported]=reported_count_dict[reported]+1
            
    # print(user_report_dict)
    # print(reported_count_dict)
    
    for user in id_list:
        if user_report_dict.get(user) is None:
            # print(f"user:{user} is nnone")
            answer.append(0)
            continue
        cnt = 0
        for user_report in user_report_dict[user]:
            reported_cnt = reported_count_dict[user_report]
            # print(f"user: {user} report {user_report} :{reported_cnt}")
            if reported_cnt>=k:
                cnt = cnt+1
        answer.append(cnt)
    
    return answer


# print(solution(
#     ["muzi", "frodo", "apeach", "neo"],
#     	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	,
#      2
# ))
# print(solution(
#     ["con", "ryan"]	,
#     ["ryan con", "ryan con", "ryan con", "ryan con"]	,3
# ))