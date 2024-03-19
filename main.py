from __future__ import annotations

import random

from tqdm.auto import tqdm

from constants import ITERATIONS
from constants import NUMBER_OF_ISLANDS
from dev.island import Island
from dev.king_markov import KingMarkov
from dev.kingdom import Kingdom

islands = []

random.seed(42)
for i in range(0, NUMBER_OF_ISLANDS):
    random_population = random.randint(1, 100000)
    island = Island(population_size=random_population)
    islands.append(island)


bikini_bottum = Kingdom(islands)
bikini_bottum.setup_island_order()
bikini_bottum.print()

markov = KingMarkov(kingdom=bikini_bottum, starting_island_id=0)

for i in tqdm(
    range(0, int(ITERATIONS)),
    desc='King Markov is traveling', ncols=80,
):
    markov.identify_next_candidate()
    markov.move_or_stay()

bikini_bottum.print()
bikini_bottum.plot_visits(name='island_visits')
