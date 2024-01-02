import Rats
import pygame


def create_new_rats(population_size, rats_picture):
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


def move(rat, gene_index, screen):
        if rat.get_genome()[gene_index] == "N": 
            screen.blit(rat.sprites_img[0], [rat.rect.x, rat.rect.y])
            if rat.rect.y >= 20:
                rat.update(0, -5)
            
        elif rat.get_genome()[gene_index] == "S":
            screen.blit(rat.sprites_img[1], [rat.rect.x, rat.rect.y])
            if rat.rect.y <= (screen.get_height()-60):
                rat.update(0, 5)
            
        elif rat.get_genome()[gene_index] == "L":
            screen.blit(rat.sprites_img[2], [rat.rect.x, rat.rect.y])
            if rat.rect.x <= (screen.get_width()-60):
                rat.update(5, 0)

        elif rat.get_genome()[gene_index] == "W":
            screen.blit(rat.sprites_img[3], [rat.rect.x, rat.rect.y])
            if rat.rect.x >= 20:
                rat.update(-5, 0)
            
        elif rat.get_genome()[gene_index] == "X":
            screen.blit(rat.sprites_img[0], [rat.rect.x, rat.rect.y])
            rat.update(0, 0)
