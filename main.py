from __future__ import annotations

from tqdm.auto import tqdm

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

stiftung = Kingdom(working_groups)
stiftung.setup_island_order()
stiftung.print()

richer_und_maltitz = KingMarkov(kingdom=stiftung, starting_island_id=4)
name = 'Richters and Maltitz'

for i in tqdm(
    range(0, int(ITERATIONS)),
    desc=f'{name} are traveling...', ncols=120,
):
    richer_und_maltitz.identify_next_candidate()
    richer_und_maltitz.move_or_stay()
    if (i % 10 == 0):
        stiftung.plot_visits(name=f'state_{i}', iteration=i)

stiftung.print()
