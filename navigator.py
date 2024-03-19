from __future__ import annotations

import random


class Navigator:
    """Represents a navigator deciding whether to move one island forward or
    backward"""

    P_CHOOSE_FOLLOWING = 0.5

    def __init__(self):
        self._moving_probability = 0

    def is_following_island_candidate(self):
        """Identifies a new island candidate by flipping a coin.
        Returns true if the following island is chosen
        Returns false if the preceding island is chosen"""

        following_island_is_candidate = False
        x = random.random()

        if (x > self.P_CHOOSE_FOLLOWING):
            following_island_is_candidate = True

        return following_island_is_candidate

    def get_moving_probability(
        self,
        current_population: int,
        candidate_population: int,
    ):
        """Determines the probability to which King Markov will go to the
        candidate island or no"""

        p = min(candidate_population/current_population, 1)

        return p
