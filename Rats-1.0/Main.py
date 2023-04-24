import pygame
import sys
import time
from threading import Thread

import RatsFunctions
import ScreenFunctions
import TargetFunctions
import AlgorithmFunctions

rats_picture = "\\Rats-1.0\\images\\mouse.png"
target_image = "\\Rats-1.0\\images\\cheese.png"

population_size = 500

screen_width = 800
screen_height = 800

not_ready = True
current_time = 0
rats_begin_time = 0
gene_index = 0
time_to_live = 8000
genome_size = 200
generation_count = 1
previus_movement_time = time.time()

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Genetic Algorithm")

screen = ScreenFunctions.create_screen(screen_width, screen_height)
target_filled_group = TargetFunctions.initialize_target(target_image, screen_width / 2, 100)

rats_filled_groups = RatsFunctions.initialize_rats(population_size, rats_picture)
AlgorithmFunctions.random_rats_genomes(rats_filled_groups, genome_size)

while True:
    screen.fill('white')

    TargetFunctions.draw_and_update_target_group(screen, target_filled_group)

    delta_time = time.time() - previus_movement_time
    previus_movement_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not_ready:
            if event.type == pygame.MOUSEBUTTONDOWN:
                rats_start_position = RatsFunctions.set_rats_start_position(rats_filled_groups, pygame.mouse.get_pos())
                rats_begin_time = pygame.time.get_ticks()
                not_ready = False

    current_time = pygame.time.get_ticks()

    if not not_ready:
        if ((current_time - rats_begin_time) < time_to_live) and (gene_index < genome_size):
            for group in rats_filled_groups:
                t = Thread(target=group.sprites()[0].move, args=(gene_index, screen, delta_time))
                t.start()
            gene_index += 1
            t.join()
        else:
            ranked_rats = AlgorithmFunctions.ranking_rats(rats_filled_groups, target_filled_group)
            best_rats = AlgorithmFunctions.get_best_rats(ranked_rats)
            rats_new_gen = RatsFunctions.initialize_rats(population_size, rats_picture)

            # settar distancia antiga
            AlgorithmFunctions.set_previus_distances(ranked_rats, rats_new_gen)

            AlgorithmFunctions.new_genomes(best_rats, rats_new_gen)
            AlgorithmFunctions.kill_rats(rats_filled_groups)
            RatsFunctions.set_rats_start_position(rats_new_gen, rats_start_position)
            rats_filled_groups = rats_new_gen
            gene_index = 0
            rats_begin_time = pygame.time.get_ticks()
            print(f"GENERATION: {generation_count} BEST SCORE: {best_rats[0][1][0]} DISTANCE FROM TARGET: {best_rats[0][1][1]}")
            print(f"=== NEXT GEN ===")
            generation_count += 1

    pygame.display.flip()
    clock.tick(60)
