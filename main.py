from __future__ import annotations

import random

from tqdm.auto import tqdm

from constants import GENERATE_GIF
from constants import ITERATIONS
from constants import NUMBER_OF_ISLANDS
from dev.island import Island
from dev.king_markov import KingMarkov
from dev.kingdom import Kingdom

islands = []

for i in range(0, NUMBER_OF_ISLANDS):
    MIN_POPULATION = 100
    MAX_POPULATION = 5000
    random_population = random.randint(MIN_POPULATION, MAX_POPULATION)
    island = Island(population_size=random_population)

    islands.append(island)


kingdom = Kingdom(islands)
kingdom.setup_island_order()
kingdom.print()

king_markov = KingMarkov(kingdom=kingdom, starting_island_id=3)
NAME = 'Markov'

for i in tqdm(
    range(0, ITERATIONS),
    desc=f'{NAME} is traveling...', ncols=100,
):
    if (GENERATE_GIF is True):
        kingdom.plot_visits(name=f'state_{i}', iteration=i)

    king_markov.identify_next_candidate()
    king_markov.move_or_stay()

if (GENERATE_GIF is True):
    kingdom.generate_gif(title='trip')
    print('GIF generated')
else:
    kingdom.plot_visits(name='visits', iteration=ITERATIONS)
    print('Plot generated.')
kingdom.print()
