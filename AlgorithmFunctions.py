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
        ranked_rats.append((group.sprites()[0], calculate_distances_from_target(group.sprites()[0], target_group)))
    return sorted(ranked_rats, key=lambda x: x[1])


def get_best_rats(ranked_rats):
    return ranked_rats[:round(len(ranked_rats) * 0.02)] # quantidade de ratos limitada


def calculate_distances_from_target(rat, target_group):  # falta encerrar o programa quando chegar no alvo
    return int(math.hypot(target_group.sprites()[0].rect.center[0] - rat.get_position()[0], target_group.sprites()[0].rect.center[1] - rat.get_position()[1]))


def new_genomes(best_rats, rats_new_gen):
    gene_pool = []
    rat_genome_len = len(best_rats[0][0].get_genome())

    for rat_tuple in best_rats:
        for gene in rat_tuple[0].get_genome():
            gene_pool.append(gene)
    for group in rats_new_gen:
        new_genome = []
        for _ in range(rat_genome_len):
            new_genome.append(random.choice(gene_pool))
        group.sprites()[0].set_genome(new_genome)


def kill_rats(rat_groups):
    for _ in range(len(rat_groups)):
        rat_groups.pop()
