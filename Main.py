import pygame
import sys
import time
from threading import Thread

import RatsFunctions
import Target
import AlgorithmFunctions


# VARIABLES 
rats_img_path = ".\\images\\mouse_N.png"
target_img_path = ".\\images\\cheese.png"

population_size = 500
mouse_position = [0, 0]
ready = False
current_time = 0
rats_begin_time = 0
gene_index = 0
time_to_live = 12000
genome_size = 200
generation_count = 1
previous_movement_time = time.time()

# TARGET
target_group = pygame.sprite.Group()
target = Target.create_target(target_img_path, (800 - 45), (800 - 90))
target_group.add(target)

# RATS
rats_groups = RatsFunctions.create_new_rats(population_size, rats_img_path)

# GENOME
AlgorithmFunctions.random_rats_genomes(rats_groups, genome_size)

# WINDOW CONFIGURATION
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Genetic Algorithm")
screen = pygame.display.set_mode((800, 800))

walls = pygame.image.load(".\\images\\wall.jpg")
walls_size = pygame.transform.scale(walls, (800, 800))

while True:
    screen.blit(walls_size, (0, 0))
    Target.draw_and_update_target_group(screen, target_group)

    previous_movement_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not ready:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                rats_start_position = RatsFunctions.set_rats_start_position(rats_groups, mouse_position)
                rats_begin_time = pygame.time.get_ticks()
                ready = True

    current_time = pygame.time.get_ticks()

    if ready:
        if ((current_time - rats_begin_time) < time_to_live) and (gene_index < genome_size):
            for group in rats_groups:
                t = Thread(target=RatsFunctions.move, args=(group.sprites()[0], gene_index, screen))
                t.start()
            gene_index += 1
            t.join()
        else:

            best_rats = AlgorithmFunctions.ranking_rats(rats_groups, target_group)
            rats_new_gen = RatsFunctions.create_new_rats(population_size, rats_img_path)
            AlgorithmFunctions.new_genomes(best_rats, rats_new_gen, genome_size)
            RatsFunctions.set_rats_start_position(rats_new_gen, mouse_position)

            for old_rats_groups, new_rats_groups in zip(rats_groups, rats_new_gen):
                for old_rat, new_rat in zip (old_rats_groups, new_rats_groups):
                    new_rat.set_distance(old_rat.get_distance())

            rats_groups = rats_new_gen
            gene_index = 0
            rats_begin_time = pygame.time.get_ticks()

            print(f"GENERATION: {generation_count} BEST SCORE: {best_rats[0][1]}")
            print(f"=== NEXT GEN ===")
            generation_count += 1

    pygame.display.flip()
    clock.tick(60)
