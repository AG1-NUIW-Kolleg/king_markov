from __future__ import annotations

from tqdm.auto import tqdm

from island import Island
from king_markov import KingMarkov
from kingdom import Kingdom


ITERATIONS = 1e7

island_0 = Island(population_size=100)
island_1 = Island(population_size=200)
island_2 = Island(population_size=300)
island_3 = Island(population_size=400)
island_4 = Island(population_size=500)
islands = [island_0, island_1, island_2, island_3, island_4]
bikini_bottum = Kingdom(islands)

bikini_bottum.setup_island_order()

markov = KingMarkov(starting_island_id=0)
for i in tqdm(
    range(0, int(ITERATIONS)),
    desc='King Markov is traveling', ncols=80,
):
    markov.identify_next_candidate(kingdom=bikini_bottum)
    markov.move(kingdom=bikini_bottum)

bikini_bottum.print()
