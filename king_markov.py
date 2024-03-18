from __future__ import annotations

from island import Island
from navigator import Navigator


class KingMarkov:
    """Represents King Markov, who is visiting different island of his
    kingdom. He wants to visit an every island in proportion to their
    population size"""

    def __init__(self, starting_island: Island):
        self._current_island = starting_island
        self._next_potential_island: Island = Island()

        self._navigatior = Navigator()
