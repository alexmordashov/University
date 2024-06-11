import pygame


class Button:
    def __init__(self, x, y, width, height, text, font, border_color=(0, 0, 0), main_color=(255, 255, 255), hover_color=(255, 0, 0),
                 clicked_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        '''self.pad_x = 20  # Default padding for the button width
        self.pad_y = 10'''  # Default padding for the button height
        self.text = text
        self.main_color = main_color
        self.border_color = border_color
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, font)  # Default font and font size
        self.is_hovered = False  # Flag to track if the button is being hovered over
        self.is_clicked = False
        self.border = pygame.Rect(self.x, self.y, self.width, self.height)
        self.main_rect = pygame.Rect(self.x + 1, self.y + 1, self.width - 2, self.height - 2)
        self.clicked_rect = pygame.Rect(self.x + 2, self.y + 2, self.width - 4, self.height - 4)


    def draw(self, window):
        # Draw the button on the provided window
        if self.is_clicked:
            pygame.draw.rect(window, self.border_color, self.border)
            pygame.draw.rect(window, self.clicked_color, self.clicked_rect)
        elif self.is_hovered:
            pygame.draw.rect(window, self.border_color, self.border)
            pygame.draw.rect(window, self.hover_color, self.main_rect)
        else:
            pygame.draw.rect(window, self.border_color, self.border)
            pygame.draw.rect(window, self.main_color, self.main_rect)


        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.main_rect.center
        window.blit(text_surface, text_rect)

    def on_click(self, action=True):
        if action:
            self.is_clicked = True
        else:
            self.is_clicked = False

    def on_hover(self, action=True):
        if action:
            self.is_hovered = True
        else:
            self.is_hovered = False

    # убрать
    '''def update_dimensions(self):
        # Update the dimensions of the button based on the text and font size
        text_surface = self.font.render(self.text, True, self.text_color)
        self.width, self.height = text_surface.get_size()

    def set_padding(self, pad_x, pad_y):
        # Set the padding for the button width and height and update the dimensions# Set the padding for the button width and height and update the dimensions
        self.pad_x, self.pad_y = pad_x, pad_y
        self.update_dimensions()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width + self.pad_x, self.height + self.pad_y)

    def set_pos(self, x_pos, y_pos):
        # Set the position of the button and update the rect
        self.x_pos, self.y_pos = x_pos, y_pos
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width + self.pad_x, self.height + self.pad_y)

    def set_text(self, text):
        # Set the text of the button and update the dimensions and rect
        self.text = text
        self.update_dimensions()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width + self.pad_x, self.height + self.pad_y)

    def set_color(self, colour):
        # Set the button color
        self.color = colour

    def set_hover_color(self, hover_color):
        # Set the button color when hovering
        self.hover_color = hover_color

    def set_text_color(self, text_color):
        # Set the text color
        self.text_color = text_color

    def set_font(self, font_name, font_size):
        # Set the font and font size for the button text and update dimensions and rect
        self.font = pygame.font.Font(font_name, font_size)
        self.update_dimensions()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width + self.pad_x, self.height + self.pad_y)
'''
