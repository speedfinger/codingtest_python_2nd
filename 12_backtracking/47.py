""" 
"""
answer = []
TARGET_NUMBER= 10
def backtracking(start_number,N, sum,arr:list):
    global answer
    print(f"start:{start_number} / sum:{sum}, {arr}")
    
    if sum == TARGET_NUMBER:
        answer.append(arr)
        return
    
    
    for num in range(start_number+1,N+1):
        
        tmp_sum=sum+num
            
        if tmp_sum>TARGET_NUMBER:
            return
        
        # backtracking(start_number+1,N,sum+num,arr+[num])
        backtracking(num,N,sum+num,arr+[num])
        
        

def solution (N) ->list:
    
    
    
    for i in range(1,N+1):
        # print(i)
        backtracking(i,N, i,[i])
        
    print()
    print(answer)
    
    return


solution(7)