from __future__ import annotations

from constants import VERBOSE
from dev.kingdom import Kingdom
from dev.navigator import Navigator


class KingMarkov:
    """Represents King Markov, who is visiting different island of his
    kingdom. He wants to visit an every island in proportion to their
    population size"""

    def __init__(self, kingdom: Kingdom, starting_island_id: int):
        self._kingdom = kingdom

        self._current_island_id = starting_island_id
        self._candidate_island_id = 0

        self._navigatior = Navigator()

    def identify_next_candidate(self):
        """Identifies the next candidate with the help of the navigator"""
        is_following_candidate = (
            self._navigatior.is_following_island_candidate()
        )

        current_island = self._kingdom.get_island_by_id(
            self._current_island_id,
        )
        if (is_following_candidate is True):
            self._candidate_island_id = current_island.get_following_id()
        else:
            self._candidate_island_id = current_island.get_preceding_id()

        if VERBOSE:
            self._log_candidate()

    def move_or_stay(self):
        """Moves King Markov to another island with the probability calculated
        by the navigator"""

        current_island = self._kingdom.get_island_by_id(
            self._current_island_id,
        )
        candidate_island = self._kingdom.get_island_by_id(
            self._candidate_island_id,
        )

        current_island_population = current_island.get_population_size()
        candidate_island_population = candidate_island.get_population_size()

        will_move = self._navigatior.will_move(
            current_population=current_island_population,
            candidate_population=candidate_island_population,
        )

        if (will_move is True):
            self._visit_island(id=self._candidate_island_id)

        else:
            self._stay_on_island()

    def _stay_on_island(self):
        """Records the stay of King Markov on an isyland by updating the visit
        count of the current island"""
        self._kingdom.get_island_by_id(self._current_island_id).count_visit()
        if VERBOSE:
            print(
                f'King Markov stayed at Island {self._current_island_id}',
            )

    def _visit_island(self, id: int):
        """Records the visit of King Markov on an island by updating the
        current island id and the islands visit count"""
        self._current_island_id = id
        self._kingdom.get_island_by_id(id).count_visit()
        if VERBOSE:
            print(f'King Markov moved to Island {self._current_island_id}')

    def _log_candidate(self):
        """Prints the new potential island"""
        print(
            'King Markov considers moving to Island ' +
            f'{self._candidate_island_id}',
        )
