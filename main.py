from __future__ import annotations

from island import Island
from king_markov import KingMarkov
from kingdom import Kingdom

island_0 = Island(population_size=100)
island_1 = Island(population_size=200)
island_2 = Island(population_size=300)
island_3 = Island(population_size=400)
island_4 = Island(population_size=500)
islands = [island_0, island_1, island_2, island_3, island_4]
bikini_bottum = Kingdom(islands)

bikini_bottum.setup_island_order()
bikini_bottum.print()

markov = KingMarkov(starting_island_id=0)
markov.visit_island(id=4, kingdom=bikini_bottum)
bikini_bottum.print()
markov.identify_next_candidate(kingdom=bikini_bottum)
