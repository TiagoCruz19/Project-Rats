import math
import random


def random_rats_genomes(rats_groups, genome_size):
    directions = ["N", "S", "L", "W", "X"]

    for group in rats_groups:
        genome = []
        for rat in group:
            for _ in range(genome_size):
                genome.append(directions[random.randint(0, 4)])
            rat.set_genome(genome)


def ranking_rats(rats_groups, target_group):
    ranked_rats = []
    for group in rats_groups:
        ranked_rats.append((group.sprites()[0], calculate_rats_scores(group.sprites()[0], target_group)))
    sorted_rats = sorted(ranked_rats, key=lambda x: x[1], reverse=True)

    return sorted_rats[:round(len(sorted_rats) * 0.02)]


def calculate_rats_scores(rat, target_group): # MELHORAR CALCULO
    rat_target_distance = math.hypot(target_group.sprites()[0].rect.center[0] - rat.rect.x, target_group.sprites()[0].rect.center[1] - rat.rect.y)

    if rat.get_distance() > rat_target_distance:
        rat.set_score(10000 - rat_target_distance)
    elif rat.get_distance() < rat_target_distance:
            rat.set_score(1000 - rat_target_distance)
    elif rat_target_distance <= 3:
            rat.set_score(99999)

    rat.set_distance(rat_target_distance)
    return rat.get_score()


def new_genomes(best_rats, rats_new_gen, genome_size): # INTRODUZIR MUTAÇÕES ALEATORIAS
    gene_pool = []
    for rat in best_rats:
        for gene in rat[0].get_genome():
            gene_pool.append(gene)

    for group in rats_new_gen:
        new_genome = []
        for _ in range(genome_size):
            new_genome.append(random.choice(gene_pool))
        group.sprites()[0].set_genome(new_genome)


'''def set_previous_distances(previous_rats_groups, rats_new_gen): # SALVAR DISTANCIA MAIS EFICIENTEMENTE
    for previous_rat, new_group in zip(previous_rats_groups, rats_new_gen):
        new_group.sprites()[0].set_distance(previous_rat.sprites()[0].get_distance())'''
