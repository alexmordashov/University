import datetime

import pygame
from button import Button
from student_window import student_window
import os
import json
from student import Student
import datetime

def game():
    width = 475
    height = 600
    fps = 30
    #
    current_date = datetime.date.today()
    #
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Симулятор студента')

    '''# Создаем объект шрифта
    font = pygame.font.Font(None, 24)
    # Создайте поверхность для кнопки
    button_surface = pygame.Surface((150, 50))
    # Отображение текста на кнопке
    text = font.render('Начать игру', True, (0, 0, 0))
    text_rect = text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
    # Создайте объект pygame.Rect, который представляет границы кнопки
    button_rect_1 = pygame.Rect(125, 125, 150, 50)  # Отрегулируйте положение'''

    button_1 = Button(125, 125, 150, 50, "Начать игру", 24)
    button_2 = Button(125, 180, 150, 50, "Продолжить игру", 24)
    button_3 = Button(125, 235, 150, 50, "Выход", 24)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.main_rect.collidepoint(event.pos):
                    button_1.on_click()
                    button_1.on_hover(action=False)
                    # button_1.on_click(event.pos[0], event.pos[0], action=True)
                    button_1.draw(screen)
                    student = Student(['100', '100', '100', '100', '50', '100', current_date.strftime("%Y-%m-%d")])
                    button_1.on_click(action=False)
                    arg = student_window(student)
                    '''if not arg:
                        running = True'''
                    # running = False
                elif button_2.main_rect.collidepoint(event.pos):
                    button_2.on_click()
                    button_2.on_hover(action=False)
                    # button_1.on_click(event.pos[0], event.pos[0], action=True)
                    button_2.draw(screen)
                    if os.stat("specifications.json").st_size == 0:
                        print('У вас нет начатой игры. Начнем новую игру!')
                        student = Student(['100', '100', '100', '100', '50', '100', current_date.strftime("%Y-%m-%d")])
                    else:
                        with open('specifications.json', 'r') as f:
                            specifications = json.load(f)
                        specifications_arr = []
                        for i in specifications.keys():
                            specifications_arr.append(specifications.get(i))
                        student = Student(specifications_arr)
                    button_2.on_click(action=False)
                    student_window(student)
                    # running = False
                elif button_3.main_rect.collidepoint(event.pos):
                    button_3.on_click()
                    button_3.on_hover(action=False)
                    # button_1.on_click(event.pos[0], event.pos[0], action=True)
                    button_3.draw(screen)
                    print("Выход!")
                    button_3.on_click(action=False)
                    running = False
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

        # Проверьте, находится ли мышь над кнопкой.
        # Это создаст эффект наведения кнопки.
        '''if button_rect_1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (2, 2, 146, 46))'''
        # pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        # pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
        # Показать текст кнопки
        '''button_surface.blit(text, text_rect)
        # Нарисуйте кнопку на экране
        screen.blit(button_surface, (button_rect_1.x, button_rect_1.y))'''
        button_1.draw(screen)
        button_2.draw(screen)
        button_3.draw(screen)
        pygame.display.flip()
    pygame.quit()
