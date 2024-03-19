from __future__ import annotations

from kingdom import Kingdom
from navigator import Navigator


class KingMarkov:
    """Represents King Markov, who is visiting different island of his
    kingdom. He wants to visit an every island in proportion to their
    population size"""

    def __init__(self, starting_island_id: int):
        self._current_island_id = starting_island_id
        self._next_potential_island_id = 0

        self._navigatior = Navigator()

    def visit_island(self, id: int, kingdom: Kingdom):
        """Records the visit of King Markov on an island by updating the
        current island id and the islands visit count"""
        self._current_island_id = id
        kingdom.get_island_by_id(id).count_visit()

    def log_position(self):
        """Logs the current position of the king"""
        print(f'King Markov is on Island-ID {self._current_island_id}')
