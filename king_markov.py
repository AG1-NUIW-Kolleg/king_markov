from __future__ import annotations

from navigator import Navigator


class KingMarkov:
    """Represents King Markov, who is visiting different island of his
    kingdom. He wants to visit an every island in proportion to their
    population size"""

    def __init__(self, starting_island_id: int):
        self._current_island_id = starting_island_id
        self._next_potential_island_id = 0

        self._navigatior = Navigator()

    def log_position(self):
        """Logs the current position of the king"""
        print(f'King Markov is on Island-ID {self._current_island_id}')
