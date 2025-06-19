""" 
https://school.programmers.co.kr/learn/courses/30/lessons/42579

["classic", "pop", "classic", "classic", "pop"]	
[500, 600, 150, 800, 2500]	
[4, 1, 3, 0]
"""


from collections import defaultdict

genre_score = defaultdict(int)



class TopValues:
    def __init__(self, top_n=2):
        self.top_n = top_n
        self.data = []  # (idx, value) 튜플 리스트

    def add(self, idx, value):
        self.data.append((idx, value))
        # value 기준 내림차순 정렬
        self.data.sort(key=lambda x: x[1], reverse=True)
        # 상위 top_n개만 유지
        self.data = self.data[:self.top_n]

    def get_top(self):
        return self.data

play_score = defaultdict(TopValues)

def solution(genres, plays):
    answer = []
    for idx, genre in enumerate(genres):
        # print(f"{idx}:{genre} / {plays[idx]}")
        
        genre_score[genre]=genre_score[genre]+plays[idx]
        
        genre_top = play_score[genre]
        if genre_top is None:
            genre_top = TopValues(top_n=2)            
            # print(f"idx:{idx}/{plays[idx]} is added to :{type(genre_top)}")
            genre_top.add(idx,plays[idx])
        else:
            # print(f"idx:{idx}/{plays[idx]} is added to :{type(genre_top)}")
            genre_top.add(idx,plays[idx])
        
        play_score[genre]=genre_top
        
        
    # play_score[genre] = genre_top.get_top()
        
    
    # print(genre_score)
    sorted_keys = [k for k, v in sorted(genre_score.items(), key=lambda x: x[1], reverse=True)]
    # print(sorted_keys)
    
    for _ in sorted_keys:
        
        tmp_list = play_score[_].get_top()
        for i in tmp_list:
            answer.append(i[0])

        
    return answer


# print(solution(
# ["classic", "pop", "classic", "classic", "pop"]	
# ,[500, 600, 150, 800, 2500]	))