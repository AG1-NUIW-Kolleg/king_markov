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

    def identify_next_candidate(self, kingdom: Kingdom):
        """Identifies the next candidate with the help of the navigator"""
        is_following_candidate = (
            self._navigatior.is_following_island_candidate()
        )

        current_island = kingdom.get_island_by_id(self._current_island_id)
        if (is_following_candidate is True):
            self._next_potential_island_id = current_island.get_following_id()
        else:
            self._next_potential_island_id = current_island.get_preceding_id()

        self._log_candidate()

    def visit_island(self, id: int, kingdom: Kingdom):
        """Records the visit of King Markov on an island by updating the
        current island id and the islands visit count"""
        self._current_island_id = id
        kingdom.get_island_by_id(id).count_visit()
        self._log_position()

    def _log_candidate(self):
        """Prints the new potential island"""
        print(
            'King Markov considers moving to Island ' +
            f'{self._next_potential_island_id}',
        )

    def _log_position(self):
        """Logs the current position of the king"""
        print(f'King Markov is on Island {self._current_island_id}')
