def solution(n):
    def dfs(row, cols, diag1, diag2):
        print(f"row:{row} cols:{cols} {diag1} {diag2}")
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if col in cols or (row+col) in diag1 or (row-col) in diag2:
                continue
            count += dfs(row+1,
                         cols | {col},
                         diag1 | {row+col},
                         diag2 | {row-col})
        return count

    return dfs(0, set(), set(), set())

# 예시 실행
print(solution(4))  # 출력: 2