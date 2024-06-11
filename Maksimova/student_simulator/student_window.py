import json
import pygame
from button import Button
from food_window import food_window
from job_window import job_window
from entertainment_window import entertainment_window
from study_window import study_window
from communication_window import communication_window
import time


def student_window(student):
    width = 475
    height = 600
    fps = 30
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Симулятор студента')

    font_spec = pygame.font.Font(None, 18)
    health = font_spec.render(f'Здоровье: {student.health}', True, (0, 0, 0))
    mood = font_spec.render(f'Настроение: {student.mood}', True, (0, 0, 0))
    energy = font_spec.render(f'Энергия: {student.energy}', True, (0, 0, 0))
    iq = font_spec.render(f'Интелект: {student.iq}', True, (0, 0, 0))
    rating = font_spec.render(f'Рейтинг в универе: {student.rating}', True, (0, 0, 0))
    money = font_spec.render(f'Деньги: {student.money}', True, (0, 0, 0))
    date = font_spec.render(f'Дата: {student.date.day}.{student.date.month}.{student.date.year}', True, (0, 0, 0))

    button_width = 83
    button_height = 83
    step = 10
    font = 18
    button_1 = Button(step, height - step - button_height, button_width, button_height, "Работа", font)
    button_2 = Button(step * 2 + button_width, height - step - button_height, button_width, button_height, "Учёба",
                      font)
    button_3 = Button(step * 3 + button_width * 2, height - step - button_height, button_width, button_height,
                      "Питание", font)
    button_4 = Button(step * 4 + button_width * 3, height - step - button_height, button_width, button_height,
                      "Развлечение", font)
    button_5 = Button(step * 5 + button_width * 4, height - step - button_height, button_width, button_height,
                      "Общение", font)
    button_6 = Button(382, 10, button_width, button_height,
                      "След. день", font)

    start_time = int(time.time())
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        current_time = int(time.time())
        if (current_time - start_time) % 2 == 0 and current_time - start_time != 0:
            arg = student.next_day()
            if arg:
                # running = False
                return 0
            #

            health = font_spec.render(f'Здоровье: {"{:.1f}".format(float(student.health))}', True, (0, 0, 0))
            mood = font_spec.render(f'Настроение: {"{:.1f}".format(float(student.mood))}', True, (0, 0, 0))
            energy = font_spec.render(f'Энергия: {student.energy}', True, (0, 0, 0))
            iq = font_spec.render(f'Интелект: {student.iq}', True, (0, 0, 0))
            rating = font_spec.render(f'Рейтинг в универе: {"{:.1f}".format(float(student.rating))}', True, (0, 0, 0))
            money = font_spec.render(f'Деньги: {student.money}', True, (0, 0, 0))
            date = font_spec.render(f'Дата: {student.date.day}.{student.date.month}.{student.date.year}', True,
                                    (0, 0, 0))
            start_time = current_time
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('specifications.json', 'w') as f:
                    json.dump({"health": student.health, "mood": student.mood, "energy": student.energy,
                               "iq": student.iq, "rating": student.rating, "money": student.money,
                               "date": student.date.strftime("%Y-%m-%d")}, f)
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.main_rect.collidepoint(event.pos):
                    button_1.on_click()
                    button_1.on_hover(action=False)
                    button_1.draw(screen)
                    job_window(student, start_time)
                    pygame.display.set_caption('Симулятор студента')
                    button_1.on_click(action=False)
                    # student_window()
                elif button_2.main_rect.collidepoint(event.pos):
                    button_2.on_click()
                    button_2.on_hover(action=False)
                    button_2.draw(screen)
                    study_window(student, start_time)
                    pygame.display.set_caption('Симулятор студента')
                    button_2.on_click(action=False)
                    # student_window()
                elif button_3.main_rect.collidepoint(event.pos):
                    button_3.on_click()
                    button_3.on_hover(action=False)
                    button_3.draw(screen)
                    food_window(student, start_time)
                    pygame.display.set_caption('Симулятор студента')
                    button_3.on_click(action=False)
                    # student_window()
                elif button_4.main_rect.collidepoint(event.pos):
                    button_4.on_click()
                    button_4.on_hover(action=False)
                    button_4.draw(screen)
                    entertainment_window(student, start_time)
                    pygame.display.set_caption('Симулятор студента')
                    button_4.on_click(action=False)
                    # student_window()
                elif button_5.main_rect.collidepoint(event.pos):
                    button_5.on_click()
                    button_5.on_hover(action=False)
                    button_5.draw(screen)
                    communication_window(student, start_time)
                    pygame.display.set_caption('Симулятор студента')
                    button_5.on_click(action=False)
                    # student_window()
                elif button_6.main_rect.collidepoint(event.pos):
                    button_6.on_click()
                    button_6.on_hover(action=False)
                    button_6.draw(screen)
                    arg = student.next_day()
                    if arg:
                        # running = False
                        return 0
                    #
                    health = font_spec.render(f'Здоровье: {"{:.1f}".format(float(student.health))}', True, (0, 0, 0))
                    mood = font_spec.render(f'Настроение: {"{:.1f}".format(float(student.mood))}', True, (0, 0, 0))
                    energy = font_spec.render(f'Энергия: {student.energy}', True, (0, 0, 0))
                    iq = font_spec.render(f'Интелект: {student.iq}', True, (0, 0, 0))
                    rating = font_spec.render(f'Рейтинг в универе: {"{:.1f}".format(float(student.rating))}', True,
                                              (0, 0, 0))
                    money = font_spec.render(f'Деньги: {student.money}', True, (0, 0, 0))
                    date = font_spec.render(f'Дата: {student.date.day}.{student.date.month}.{student.date.year}', True,
                                            (0, 0, 0))
                    #
                    print(button_6.text)
                    button_6.on_click(action=False)
                    # student_window()
        if button_1.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_1.on_hover()
        elif not button_1.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_1.on_hover(action=False)
        if button_2.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_2.on_hover()
        elif not button_2.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_2.on_hover(action=False)
        if button_3.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_3.on_hover()
        elif not button_3.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_3.on_hover(action=False)
        if button_4.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_4.on_hover()
        elif not button_4.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_4.on_hover(action=False)
        if button_5.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_5.on_hover()
        elif not button_5.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_5.on_hover(action=False)
        if button_6.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_6.on_hover()
        elif not button_6.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_6.on_hover(action=False)
        button_1.draw(screen)
        button_2.draw(screen)
        button_3.draw(screen)
        button_4.draw(screen)
        button_5.draw(screen)
        button_6.draw(screen)

        screen.blit(health, (20, 20))
        screen.blit(mood, (20, 40))
        screen.blit(energy, (20, 60))
        screen.blit(iq, (20, 80))
        screen.blit(rating, (20, 100))
        screen.blit(money, (20, 120))
        screen.blit(date, (20, 140))

        pygame.display.flip()
    pygame.quit()
