"""

"""

def polynomial_hash(str):
  p = 31  # 소수
  m = 1_000_000_007  # 버킷 크기
  hash_value = 0
  for char in str:
    hash_value = (hash_value * p + ord(char)) % m
  return hash_value


def solution(str_list,query_list):
    
    hash_list = [polynomial_hash(str) for str in str_list]
        
    answer = []
    for query in query_list:
        hash_key = polynomial_hash(query)
        if hash_key in hash_list:
            answer.append(True)
        else:
            answer.append(False)
                
    
    return answer


print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"] )) # 반환값 : [True, False, False, True]


