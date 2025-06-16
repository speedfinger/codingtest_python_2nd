"""

"""
def solution(arr:list,target:int)->int :
    
    hash_arr=[0]*(target+1)
    # print(hash_arr)
    for number in arr:
        if number<target:
            hash_arr[number-1]=1
    
    
    for number in arr:
        find_number = target - number
        if find_number>=1 and find_number!=number:
            if hash_arr[find_number-1]==1:
                return True
                
                
            
        
    
    return False


print(solution([1,2,3,4,8],6))