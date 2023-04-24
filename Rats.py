import pygame


class Rat(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()

        self.genome = []
        self.speed = 100
        self.position = None
        self.image = None
        self.rect = None
        self.images = [pygame.transform.scale(pygame.image.load("D:\\Rats-1.1\\images\\mouse_N.png"), [30, 40]),
                       pygame.transform.scale(pygame.image.load("D:\\Rats-1.1\\images\\mouse_S.png"), [30, 40]),
                       pygame.transform.scale(pygame.image.load("D:\\Rats-1.1\\images\\mouse_E.png"), [30, 40]),
                       pygame.transform.scale(pygame.image.load("D:\\Rats-1.1\\images\\mouse_W.png"), [30, 40])]

    def move(self, gene_index, screen, delta_time):
        if self.get_genome()[gene_index] == "1000":
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.center = [self.get_position()[0], self.get_position()[1]]  # erro
            if "-y" not in self.verify_wall_colision(screen):
                self.rect.y -= round(self.speed * delta_time)
                self.set_position([self.get_position()[0], (self.get_position()[1] - round(self.speed * delta_time))])

        elif self.get_genome()[gene_index] == "0100":
            self.image = self.images[1]
            self.rect = self.image.get_rect()
            self.rect.center = [self.get_position()[0], self.get_position()[1]]
            if "+y" not in self.verify_wall_colision(screen):
                self.rect.y += round(self.speed * delta_time)
                self.set_position([self.get_position()[0], (self.get_position()[1] + round(self.speed * delta_time))])

        elif self.get_genome()[gene_index] == "0010":
            self.image = self.images[2]
            self.rect = self.image.get_rect()
            self.rect.center = [self.get_position()[0], self.get_position()[1]]
            if "+x" not in self.verify_wall_colision(screen):
                self.rect.x += round(self.speed * delta_time)
                self.set_position([(self.get_position()[0] + round(self.speed * delta_time)), self.get_position()[1]])

        elif self.get_genome()[gene_index] == "0001":
            self.image = self.images[3]
            self.rect = self.image.get_rect()
            self.rect.center = [self.get_position()[0], self.get_position()[1]]
            if "-x" not in self.verify_wall_colision(screen):
                self.rect.x -= round(self.speed * delta_time)
                self.set_position([(self.get_position()[0] - round(self.speed * delta_time)), self.get_position()[1]])

        if self.get_genome()[gene_index] != "0000":
            self.blit_func(screen)

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

    def get_genome(self):
        return self.genome

    def set_genome(self, _genome):
        self.genome = _genome
