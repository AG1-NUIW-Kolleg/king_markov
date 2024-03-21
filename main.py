from __future__ import annotations

from tqdm.auto import tqdm

from constants import GENERATE_GIF
from constants import ITERATIONS
from dev.island import Island
from dev.king_markov import KingMarkov
from dev.kingdom import Kingdom

working_groups = [
    Island(population_size=5),
    Island(population_size=1),
    Island(population_size=2),
    Island(population_size=1),
    Island(population_size=2),
]

kingdom = Kingdom(working_groups)
kingdom.setup_island_order()
kingdom.print()

king_markov = KingMarkov(kingdom=kingdom, starting_island_id=3)
name = 'Markov'

for i in tqdm(
    range(0, int(ITERATIONS)),
    desc=f'{name} is traveling...', ncols=100,
):
    if (GENERATE_GIF is True):
        kingdom.plot_visits(name=f'state_{i}', iteration=i)
    king_markov.identify_next_candidate()
    king_markov.move_or_stay()

if (GENERATE_GIF is True):
    kingdom.generate_gif(title='trip')
else:
    kingdom.plot_visits(name='visits', iteration=ITERATIONS)
kingdom.print()
