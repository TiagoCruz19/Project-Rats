import pygame


class Rat(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()

        self.genome = []
        self.angle = 0
        self.score = 0
        self.speed = 100
        self.position = None
        self.aux_img = None
        self.previus_distance_from_target = 99999
        self.image = pygame.transform.scale(pygame.image.load(picture_path), [30, 40])
        self.rect = self.image.get_rect()
        self.set_position(self.rect.center)

    def update(self, screen):
        pass

    def move(self, gene_index, screen, delta_time):

        if self.get_genome()[gene_index] == "1000":
            if self.angle != 0:
                self.rotate(screen, -self.angle)
                self.angle = 0
            else:
                if "-y" not in self.verify_wall_colision(screen):
                    self.rect.y -= round(self.speed * delta_time)
                    self.set_position(
                        [self.get_position()[0], (self.get_position()[1] - round(self.speed * delta_time))])

        elif self.get_genome()[gene_index] == "0100":
            if self.angle != -180:
                self.rotate(screen, (self.angle - 180))
                self.angle = -180
            else:
                if "+y" not in self.verify_wall_colision(screen):
                    self.rect.y += round(self.speed * delta_time)
                    self.set_position(
                        [self.get_position()[0], (self.get_position()[1] + round(self.speed * delta_time))])

        elif self.get_genome()[gene_index] == "0010":
            if self.angle != -90:
                self.rotate(screen, (self.angle - 90))
                self.angle = -90
            else:
                if "+x" not in self.verify_wall_colision(screen):
                    self.rect.x += round(self.speed * delta_time)
                    self.set_position(
                        [(self.get_position()[0] + round(self.speed * delta_time)), self.get_position()[1]])

        elif self.get_genome()[gene_index] == "0001":
            if self.angle != 90:
                self.rotate(screen, 90)
                self.angle = 90
            else:
                if "-x" not in self.verify_wall_colision(screen):
                    self.rect.x -= round(self.speed * delta_time)
                    self.set_position(
                        [(self.get_position()[0] - round(self.speed * delta_time)), self.get_position()[1]])

        self.blit_func(screen)

    def rotate(self, _screen, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = [self.get_position()[0], self.get_position()[1]]

    def blit_func(self, screen):
        screen.blit(self.image, [self.get_position()[0] - self.image.get_width() / 2, self.get_position()[1] - self.image.get_height() / 2])

    def verify_wall_colision(self, _screen):
        colision_str = ""
        if self.rect.top <= 0:
            colision_str += "-y"
        elif self.rect.bottom >= _screen.get_height():
            colision_str += "+y"
        if self.rect.left <= 0:
            colision_str += "-x"
        elif self.rect.right >= _screen.get_width():
            colision_str += "+x"

        return colision_str

    def get_position(self):
        return self.position

    def set_position(self, _position):
        self.position = _position

    def get_score(self):
        return self.score

    def set_score(self, _score):
        self.score = _score

    def get_genome(self):
        return self.genome

    def set_genome(self, _genome):
        self.genome = _genome

    def get_previus_distance_from_target(self):
        return self.previus_distance_from_target

    def set_previus_distance_from_target(self, _previus_distance_from_target):
        self.previus_distance_from_target = _previus_distance_from_target
