from __future__ import annotations


class Navigator:
    """Represents a navigator deciding whether to move one island forward or
    backward"""

    P_CHOOSE_PRECEDING = 0.5
    P_CHOOSE_FOLLOWING = 0.5

    def __init__(self):
        if (self.P_CHOOSE_PRECEDING + self.P_CHOOSE_FOLLOWING != 1):
            raise ValueError(
                'probabilities of choosing preceding and ' +
                ' following island should add up to 1',
            )

        self._moving_probability = 0

    def get_moving_probability(
        self,
        current_population: int,
        candidate_population: int,
    ):
        """Determines the probability to which King Markov will go to the
        candidate island or no"""

        p = min(candidate_population/current_population, 1)

        return p
