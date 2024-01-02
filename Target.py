import pygame


class create_target(pygame.sprite.Sprite):

    def __init__(self, picture_path, x, y):

        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (60, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


def draw_and_update_target_group(screen, target_group):
    target_group.draw(screen)
    target_group.update()
