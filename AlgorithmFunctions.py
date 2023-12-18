import math
import random


def random_rats_genomes(rats_groups, genome_size):
    for group in rats_groups:
        genome = []
        for rat in group:
            for _ in range(genome_size):
                genome.append(random_rats_genes())
            rat.set_genome(genome)


def random_rats_genes():
    gene_list = ["0", "0", "0", "0"]
    for gene_index in range(len(gene_list)):
        active = random.randint(0, 1)
        if "1" not in gene_list:
            gene_list[gene_index] = str(active)
    return "".join(gene_list)


def ranking_rats(rats_groups, target_group):
    ranked_rats = []
    for group in rats_groups:
        ranked_rats.append((group.sprites()[0], calculate_rats_scores(group.sprites()[0], target_group)))
    return sorted(ranked_rats, key=lambda x: x[1][0], reverse=True)


def get_best_rats(ranked_rats):
    return ranked_rats[:round(len(ranked_rats) * 0.02)]


def calculate_rats_scores(rat, target_group):
    rat_distance = calculate_distances_from_target(rat, target_group)
    if rat_distance > 0:
        if rat_distance < rat.get_previus_distance_from_target():
            rat.set_score(rat.get_score() + 1/rat_distance)  # quanto mais perto menos pontos ganha. Pensa.
        else:
            rat.set_score(rat.get_score() - 1/rat_distance)
    else:
        rat.set_score(9)

    # falta encerrar o programa quando chegar no alvo
    return [rat.get_score(), rat_distance]


def calculate_distances_from_target(rat, target_group):
    return math.hypot(target_group.sprites()[0].rect.center[0] - rat.get_position()[0], target_group.sprites()[0].rect.center[1] - rat.get_position()[1])


def set_previus_distances(ranked_rats, rats_new_gen):
    for ranked, new_group in zip(ranked_rats, rats_new_gen):
        new_group.sprites()[0].set_previus_distance_from_target(ranked[1][1])


def new_genomes(best_rats, rats_new_gen):
    gene_pool = []
    for rat in best_rats:
        for gene in rat[0].get_genome():
            gene_pool.append(gene)

    for group in rats_new_gen:
        new_genome = []
        for _ in range(len(rat[0].get_genome())):
            new_genome.append(random.choice(gene_pool))
        group.sprites()[0].set_genome(new_genome)


def kill_rats(rat_groups):
    for _ in range(len(rat_groups)):
        rat_groups.pop()
