"""
https://school.programmers.co.kr/learn/courses/30/lessons/42888

["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']
"""

def solution(record):
    answer = []
    # print(record)
    uid_names = {}
    print_list = []
    for idx, item in enumerate(record):
        # print(item)
        command, uid, *name = item.split(" ")
        # print(f"{command} / {uid} / {name}")
        
        if command =="Enter" or command =="Change":        
            uid_names[uid] = name
            
        if command == "Enter" or command =="Leave":
            print_list.append((uid,command))
    
    # print(f"{print_list}")
    
    for idx, item in enumerate(print_list):
        uid, command = item
        # print(f"{uid} / {command}")
        
        post_str = "님이 들어왔습니다." if command=="Enter" else "님이 나갔습니다."
        prev_str = uid_names[uid][0]
        # print(f"{prev_str}{post_str}")
        answer.append(f"{prev_str}{post_str}")
    
    return answer


# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


"""
unpacking
command, uid, *name = item.split(" ") 
"""