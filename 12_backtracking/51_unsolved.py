""" 
https://school.programmers.co.kr/learn/courses/30/lessons/92342

n	info	result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]


1. 만약에 높은점수인데 0 이면 1발을 무조건 쏘는게 유리
2. 하지가 않네,,점수차이가 같을땐 낮은점수를 더 많이 맞춘게 정답

최대점수차이,,
1] info에서 10점부터 ~가장 큰 점수 전까지 0을 무조건 한발만 쏜다
2] 탐색시에 중간에 0인 케이스는 무조건 한발만 쏜다

같은 화살갯수면 점수는 어피치가 먹는다.
라이언이 어떻게 화살을 쏘든 라이언의 점수가 어피치의 점수보다 낮거나 같으면 [-1]을 return 해야 합니다.

info의 길이는 11로 짧다.
2111000000
32


"""
INF  = 9999

# def find_combinations(N,info):
#     result = []
#     comb = [0] * 11

#     def backtrack(idx,remain):
#         if idx == 11:
#             if remain == 0:
#                 result.append(comb[:])
#             return
#         # 0 선택
#         comb[idx] = 0
#         backtrack(idx + 1,remain)

#         # info[idx] 선택 (단,0이 아닐 때만)
#         if info[idx] != 0 and remain - info[idx] >= 0:
#             comb[idx] = info[idx]
#             backtrack(idx + 1,remain - info[idx])

#         # info[idx]+1 선택
#         if remain - (info[idx] + 1) >= 0:
#             comb[idx] = info[idx] + 1
#             backtrack(idx + 1,remain - (info[idx] + 1))

#     backtrack(0,N)
#     return result
def find_combinations(N, info):
    result = []
    comb = [0] * 11

    def backtrack(idx, remain):
        if idx == 11:
            if remain == 0:
                result.append(comb[:])
            return
        if idx < 10:
            # 0 선택
            comb[idx] = 0
            backtrack(idx + 1, remain)
            # info[idx] 선택 (단, 0이 아닐 때만)
            if info[idx] != 0 and remain - info[idx] >= 0:
                comb[idx] = info[idx]
                backtrack(idx + 1, remain - info[idx])
            # info[idx]+1 선택
            if remain - (info[idx] + 1) >= 0:
                comb[idx] = info[idx] + 1
                backtrack(idx + 1, remain - (info[idx] + 1))
        else:
            # 마지막 인덱스: 0 ~ remain까지 아무 값이나 가능
            for val in range(remain + 1):
                comb[idx] = val
                backtrack(idx + 1, remain - val)

    backtrack(0, N)
    return result

def is_better(new_arr,old_arr):
    # 뒤에서부터 비교
    for i in range(10,-1,-1):
        if new_arr[i] > old_arr[i]:
            return True  # 새 배열이 더 우선
        elif new_arr[i] < old_arr[i]:
            return False # 기존 배열이 더 우선
    return False  # 완전히 같으면 기존 유지

def _sum_two_arr(apache,lion):
    apache_sum =0
    lion_sum=0
    for idx,_ in enumerate(apache):
        apache_cnt =apache[idx]
        line_cnt = lion[idx]
        
        if apache_cnt==0 and line_cnt==0:
            continue
        
        if apache_cnt>=line_cnt:
            apache_sum=apache_sum+(10-idx)
            # print(f"apache win : {idx}: {(10-idx)}")
        else:
            lion_sum=lion_sum+(10-idx)
            # print(f"lion win : {idx}: {(10-idx)}")
    
    return apache_sum,lion_sum

def solution(n,info):
    answer = [-1]
    length_of_info = len(info)
    
    # is_hitted = [False for _ in range(length_of_info)]    
    # for idx,hitted in enumerate(info):
    #     if hitted !=0:
    #         is_hitted[idx]=True
    # print(is_hitted)
    
    # 1 0 1 1
    
    """ 
    라이언의 화살수보다 같거나 +1개 많게 
    아니면 0
    """
    
    lion_shots = find_combinations(n,info)
    # lion_shots=[]
    # from itertools import combinations_with_replacement
    # for combi in combinations_with_replacement(range(11), n):
    #     print(combi)
    #     lion_shots.append(combi)
    # print(lion_shots)
    max_abs = -1
    from collections import defaultdict
    lion_max_shots = defaultdict(list)
    for lion_arr in lion_shots:
        apache,lion = _sum_two_arr(info,lion_arr)
        
        if lion>apache:
            max_abs=max(max_abs,lion-apache)
            if lion in lion_max_shots:
                # 기존 배열과 비교
                if is_better(lion_arr,lion_max_shots[lion]):
                    lion_max_shots[lion] = lion_arr
            else:
                lion_max_shots[lion] = lion_arr

    
    # print(f"apache:{apache} lion: {lion}")
    # print(lion_max_shots)
    if lion_max_shots :
        max_arr = lion_max_shots[max(lion_max_shots)]
        # print(max_arr)
        return max_arr
    
    
    return answer


# print(solution(
#     5,	[2,1,1,1,0,0,0,0,0,0,0] #[0,2,2,0,1,0,0,0,0,0,0]
# ))
# print(solution(
#   9,[0,0,1,2,0,1,1,1,1,1,1]  
# ))
# print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))
# [1,1,1,1,1,1,1,0,0,0,3]
# [1,1,1,1,1,1,1,1,0,0,2]