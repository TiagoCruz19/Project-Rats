import pygame


class Rat(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()

        self.genome = []
        self.score = 0
        self.distance = 99999
        self.sprites_img = [
            pygame.transform.scale(pygame.image.load(".\\images\\mouse_N.png"), [30, 40]),
            pygame.transform.scale(pygame.image.load(".\\images\\mouse_S.png"), [30, 40]),
            pygame.transform.scale(pygame.image.load(".\\images\\mouse_L.png"), [40, 30]),
            pygame.transform.scale(pygame.image.load(".\\images\\mouse_W.png"), [40, 30])
        ]
        self.rect = self.sprites_img[0].get_rect()

    def update(self, move_x, move_y):
        self.rect.move_ip(move_x, move_y)

    def get_score(self):
        return self.score

    def set_score(self, _score):
        self.score = _score

    def get_genome(self):
        return self.genome

    def set_genome(self, _genome):
        self.genome = _genome

    def get_distance(self):
        return self.distance

    def set_distance(self, _distance):
        self.distance = _distance
