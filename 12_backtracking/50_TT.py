""" 
https://school.programmers.co.kr/learn/courses/30/lessons/12952


대각선 방향을 체크하는 공식을 모르면 풀 수 가 있나???

"""

def _pprint(arr):
    for _ in arr:
        print(_)
    print()


    

def solution(n):
    answer = 0
    
    # print(n)
    chess_map = [[0 for _ in range(0,n)] for _ in range(0,n)]
    # _pprint(chess_map)
    
    # for y in range(0,n):
    #     for x in range(0,n):
    #         chess_map[y][x]=1
            
    #         _pprint(chess_map)
    #         chess_map[y][x]=0
    
        
    for first_row_column in range(0,n):
        chess_map[0][first_row_column]=1
        # _pprint(chess_map)
        
        for next_row in range(1,n):
            for columns in range(0,n):
                chess_map[next_row][columns]=1
                _pprint(chess_map)
                chess_map[next_row][columns]=0
        
        chess_map[0][first_row_column]=0
            
    
    
    return answer

print(solution(4))