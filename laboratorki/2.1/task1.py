def count_jewels(J, S):
    jewels = set(J)
    count = 0

    for char in S:
        if char in jewels:
            count += 1

    return count

if __name__ == "__main__":
    J = input("Введите строку с драгоценностями (J): ")
    S = input("Введите строку с камнями (S): ")

    result = count_jewels(J, S)
    print(f"Количество драгоценностей среди камней: {result}")