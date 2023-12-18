import pygame
import sys
import time
from threading import Thread

import RatsFunctions
import Target
import AlgorithmFunctions

# VARIABLES 
rats_img_path = ".\\images\\mouse.png"
target_img_path = ".\\images\\cheese.png"

population_size = 500
screen_width = 800
screen_height = 800
mouse_position = [0, 0]
not_ready = True
current_time = 0
rats_begin_time = 0
gene_index = 0
time_to_live = 8000
genome_size = 200
generation_count = 1
previous_movement_time = time.time()


# WINDOW CONFIGURATION
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Genetic Algorithm")
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill('white')

# TARGET
target_group = pygame.sprite.Group()
target = Target.create_target(target_img_path, (screen_width - 30), 50)
target_group.add(target)

# RATS
rats_groups = RatsFunctions.create_rats(population_size, rats_img_path)

# GENOME
AlgorithmFunctions.random_rats_genomes(rats_groups, genome_size)

while True:

    #temp
    screen.fill('white')
    #----

    Target.draw_and_update_target_group(screen, target_group)

    delta_time = time.time() - previous_movement_time
    previous_movement_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not_ready:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                rats_start_position = RatsFunctions.set_rats_start_position(rats_groups, mouse_position)
                rats_begin_time = pygame.time.get_ticks()
                not_ready = False

    current_time = pygame.time.get_ticks()

    if not not_ready:
        if ((current_time - rats_begin_time) < time_to_live) and (gene_index < genome_size):
            for group in rats_groups:
                t = Thread(target=RatsFunctions.move, args=(group.sprites()[0], gene_index, screen, delta_time))
                t.start()
            gene_index += 1
            t.join()
        else:
            best_rats = AlgorithmFunctions.ranking_rats(rats_groups, target_group)
            rats_new_gen = RatsFunctions.create_rats(population_size, rats_img_path)

            # settar distancia antiga
            AlgorithmFunctions.set_previous_distances(rats_groups, rats_new_gen)

            AlgorithmFunctions.new_genomes(best_rats, rats_new_gen, genome_size)


            AlgorithmFunctions.kill_rats(rats_groups)
            RatsFunctions.set_rats_start_position(rats_new_gen, mouse_position)

            rats_groups = rats_new_gen
            gene_index = 0
            rats_begin_time = pygame.time.get_ticks()

            print(f"GENERATION: {generation_count} BEST SCORE: {best_rats[0][1]}")
            print(f"=== NEXT GEN ===")
            generation_count += 1

    pygame.display.flip()
    clock.tick(60)
