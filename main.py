from __future__ import annotations

from tqdm.auto import tqdm

from island import Island
from king_markov import KingMarkov
from kingdom import Kingdom


ITERATIONS = 1e8

iceland = Island(population_size=100)
new_zealand = Island(population_size=200)
madagaskar = Island(population_size=300)
great_britain = Island(population_size=400)
australia = Island(population_size=500)
islands = [iceland, new_zealand, madagaskar, great_britain, australia]
bikini_bottum = Kingdom(islands)

bikini_bottum.setup_island_order()

markov = KingMarkov(kingdom=bikini_bottum, starting_island_id=0)

for i in tqdm(
    range(0, int(ITERATIONS)),
    desc='King Markov is traveling', ncols=80,
):
    markov.identify_next_candidate()
    markov.move_or_stay()

bikini_bottum.print()
