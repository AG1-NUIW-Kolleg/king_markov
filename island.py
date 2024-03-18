from __future__ import annotations


class Island:
    """Represents an island with an ID and a population size"""

    def __init__(self, island_id=0, population_size=0):
        self._id = island_id
        self._population_size = population_size
