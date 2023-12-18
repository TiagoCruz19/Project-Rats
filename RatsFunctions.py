import Rats
import pygame


def create_rats(population_size, rats_picture):
    rat_groups = []

    for x in range(population_size):
        rat_groups.append(pygame.sprite.Group())
        rat_groups[x].add(Rats.Rat(rats_picture))

    return rat_groups


def set_rats_start_position(rats_groups, mouse_position):
    for group in rats_groups:
        for rat in group:
            rat.rect.x = mouse_position[0]
            rat.rect.y = mouse_position[1]


'''def rotate(self, _screen, angle):
    self.image = pygame.transform.rotate(self.image, angle)
    self.rect = self.image.get_rect()
    self.rect.center = [self.get_position()[0], self.get_position()[1]]'''


def move(rat, gene_index, screen, delta_time):
        if rat.get_genome()[gene_index] == "N":
            if rat.rect.y >= 20:
                rat.rect.y -= round(rat.speed * delta_time)
            
        elif rat.get_genome()[gene_index] == "S":
            if rat.rect.y <= (screen.get_height()-60):
                rat.rect.y += round(rat.speed * delta_time)
            
        elif rat.get_genome()[gene_index] == "L":
            if rat.rect.x <= (screen.get_width()-50):
                rat.rect.x += round(rat.speed * delta_time)
            
        elif rat.get_genome()[gene_index] == "W":
            if rat.rect.x >= 20:
                rat.rect.x -= round(rat.speed * delta_time)
            
        elif rat.get_genome()[gene_index] == "X":
            rat.rect.y = rat.rect.y
            rat.rect.x = rat.rect.x

        screen.blit(rat.image, [rat.rect.x, rat.rect.y])
