import random

def generate_successful_arrangement():
    queens = list(range(8))
    random.shuffle(queens)
    return queens

def check_queens(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                return False
    return True

def find_successful_arrangements():
    successful_arrangements = []
    attempts = 0

    while len(successful_arrangements) < 4:
        queens = generate_successful_arrangement()
        if check_queens(queens):
            successful_arrangements.append(queens)
        attempts += 1

    return successful_arrangements, attempts


if __name__ == "__main__":
    successful_arrangements, attempts = find_successful_arrangements()

    print(f"Успешные расстановки ферзей (всего попыток: {attempts}):")
    for arrangement in successful_arrangements:
        print(arrangement)
