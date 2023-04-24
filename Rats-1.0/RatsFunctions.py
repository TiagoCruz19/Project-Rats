import Rats
import pygame


def initialize_rats(population_size, rats_picture):
    rats = create_rats(population_size, rats_picture)
    rats_empty_groups = create_empty_groups_for_rats(rats)
    insert_rats_in_groups(rats_empty_groups, rats)
    return rats_empty_groups


def create_rats(population_size, rats_picture):
    rats = []
    for _ in range(population_size):
        rats.append(Rats.Rat(rats_picture))
    return rats


def create_empty_groups_for_rats(rats):
    rats_groups = []
    for _ in range(len(rats)):
        rats_groups.append(pygame.sprite.Group())
    return rats_groups


def insert_rats_in_groups(rats_empty_groups, rats):
    for _ in range(len(rats_empty_groups)):
        rats_empty_groups[_].add(rats[_])


def set_rats_start_position(rats_groups, mouse_position):
    for group in rats_groups:
        for rat in group:
            rat.set_position(mouse_position)
    return mouse_position
