def combination_sum(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    candidates = list(map(int, input("Введите числа через пробел: ").split()))
    target = int(input("Введите целевую сумму: "))

    combinations = combination_sum(candidates, target)

    print(f"Найдено {len(combinations)} комбинаций:")
    for combo in combinations:
        print(combo)