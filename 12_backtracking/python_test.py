from itertools import combinations_with_replacement
from collections import Counter

n = 5
for combi in combinations_with_replacement(range(11), 2):
    print(combi)
    cnt = Counter(combi)
    # print(cnt)
    