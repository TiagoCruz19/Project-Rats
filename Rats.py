import pygame


class Rat(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()

        self.genome = []
        self.score = 0
        self.speed = 100
        self.previous_target_distance = 99999
        self.image = pygame.transform.scale(pygame.image.load(picture_path), [30, 40])
        self.rect = self.image.get_rect()

    def get_score(self):
        return self.score

    def set_score(self, _score):
        self.score = _score

    def get_genome(self):
        return self.genome

    def set_genome(self, _genome):
        self.genome = _genome

    def get_previous_target_distance(self):
        return self.previous_target_distance

    def set_previous_target_distance(self, _previous_target_distance):
        self.previous_target_distance = _previous_target_distance
