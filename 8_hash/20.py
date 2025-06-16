"""
https://school.programmers.co.kr/learn/courses/30/lessons/42576

participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

"""
from collections import defaultdict
  
def solution(participant, completion):
    str_dict = defaultdict(int)
    
    for _ in completion:
      cnt = str_dict[_]
      if cnt !=0:
        str_dict[_]=cnt+1
      else:
        str_dict[_]=1
    
    for _ in participant:
      cnt = str_dict[_]
      if cnt==0:
        return _
      else:
        str_dict[_] = cnt -1
        
    
    return ""
    
# print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"]))    
# print(solution(["mislav", "stanko", "mislav", "ana"]	,["stanko", "ana", "mislav"]))
