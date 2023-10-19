import random


def monty_hall(n):
    choice_1_win = 0  # количестов побед, когда игрок согласился изменить выбор
    choice_2_win = 0  # количестов побед, когда игрок не согласился изменить выбор
    win_count = 0
    for i in range(n):
        priz_place = random.randrange(1, 4)
        computer_choice = random.randrange(1, 4)
        leader_choice = [i for i in range(1, 4) if
                         i != priz_place and i != computer_choice][0]  # ведущий выбрал дверь, где точно нет приза
        choice_2 = random.choice([1, 0])  # 1 - да, 0 - нет (игрок делает выбор: сменить дверь или нет)
        if choice_2:
            if (6 - computer_choice - leader_choice) == priz_place:  # проверка второго выбора игрока
                choice_2_win += 1
                win_count += 1
        else:
            if computer_choice == priz_place:
                choice_1_win += 1
                win_count += 1
    return f'Шанс увеличится на {int(choice_2_win / win_count * 100) - int(choice_1_win/ win_count * 100)} процента'