import pygame
import sys
import time
from threading import Thread

import RatsFunctions
import ScreenFunctions
import TargetFunctions
import AlgorithmFunctions

rats_picture = "D:\\Rats-1.1\\images\\mouse_N.png"
target_image = "D:\\Rats-1.1\\images\\cheese.png"
screen_width = 800
screen_height = 800

gene_index = 0
generation_count = 1

genome_size = 200
population_size = 500

first = True

previus_movement_time = time.time()

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Genetic Algorithm")

screen = ScreenFunctions.create_screen(screen_width, screen_height)
target_filled_group = TargetFunctions.initialize_target(target_image, screen_width - 25, screen_height - 25)  # !HardCode! deveria poder ter posicionamneto dinamico. Pensa.

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
        if first:
            if event.type == pygame.MOUSEBUTTONDOWN:
                rats_start_position = RatsFunctions.set_rats_start_position(rats_filled_groups, pygame.mouse.get_pos())
                first = False

    if not first:
        if gene_index < genome_size:
            for group in rats_filled_groups:
                t = Thread(target=group.sprites()[0].move, args=(gene_index, screen, delta_time))#  delta_time não será sempre +ou- 0.85. Pensa.
                t.start()
            gene_index += 1
        else:
            ranked_rats = AlgorithmFunctions.ranking_rats(rats_filled_groups, target_filled_group)
            best_rats = AlgorithmFunctions.get_best_rats(ranked_rats)
            rats_new_gen = RatsFunctions.initialize_rats(population_size, rats_picture)
            AlgorithmFunctions.new_genomes(best_rats, rats_new_gen)
            AlgorithmFunctions.kill_rats(rats_filled_groups)
            RatsFunctions.set_rats_start_position(rats_new_gen, rats_start_position)
            rats_filled_groups = rats_new_gen
            gene_index = 0
            print(f"GENERATION: {generation_count} DISTANCE FROM TARGET: {best_rats[0][1]}")
            print(f"=== NEXT GEN ===")
            generation_count += 1

    pygame.display.flip()
    clock.tick(60)
