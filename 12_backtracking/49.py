"""
https://school.programmers.co.kr/learn/courses/30/lessons/87946  
80	[[80,20],[50,40],[30,10]]	3
"""
from itertools import permutations

def number_combinations(N):
    nums = list(range(1, N+1))
    return list(permutations(nums))


def solution(k, dungeons):
    answer = 0
    
    life = k 
    
    stage_number_of_dungeon = len(dungeons)    
    result = number_combinations(stage_number_of_dungeon)
    for comb in result:
        life = k 
        stage_pass_cnt = 0
        for stage in comb:
            need_life,decrease_life = dungeons[stage-1]
            # print(f"{stage-1} need : {need_life} and will be decrease : {decrease_life}")
            if need_life>life:
                continue
            life = life-decrease_life
            stage_pass_cnt+=1
        
        answer = max(answer,stage_pass_cnt)
    
    
    return answer


print(solution(
    80,
    [[80,20],[50,40],[30,10]]
))