import pygame


class Target(pygame.sprite.Sprite):

    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
