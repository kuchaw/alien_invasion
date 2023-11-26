import pygame.font


class Button():
    def __init__(self, ai_settings, screen, msg):
        """initialize button atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #build thr buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #the button message need to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """turn into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center =self.rect.center
    def draw_button(self):
        #draw blank button and then message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)