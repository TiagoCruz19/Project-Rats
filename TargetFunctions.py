import pygame
import Target


def initialize_target(target_image, target_x, target_y):
    target = create_target(target_image, target_x, target_y)
    target_empty_group = create_empty_target_group()
    insert_target_in_group(target_empty_group, target)
    return target_empty_group


def create_target(target_image, target_x, target_y):
    return Target.Target(target_image, target_x, target_y)


def create_empty_target_group():
    return pygame.sprite.Group()


def insert_target_in_group(target_empty_group, target):
    target_empty_group.add(target)


def draw_and_update_target_group(screen, target_group):
    target_group.draw(screen)
    target_group.update()
