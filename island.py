from __future__ import annotations


class Island:
    """Represents an island with an ID and a population size"""

    def __init__(self, population_size=0):
        self._population_size = population_size
        self._id = 0
        self._preceding_id = 0
        self._following_id = 0

    def get_population_size(self) -> int:
        """Returns the population size"""
        return self._population_size

    def get_id(self) -> int:
        """Returns the id of the island"""
        return self._id

    def get_preceding_id(self) -> int:
        """Returns the preceding islands id"""
        return self._preceding_id

    def get_following_id(self) -> int:
        """Returns the following islands id"""
        return self._following_id

    def set_id(self, id: int):
        """Sets the islands id"""
        self._id = id

    def set_preceding_id(self, id: int):
        """Sets the preceding islands id"""
        self._preceding_id = id

    def set_following_id(self, id: int):
        """Sets the following islands id"""
        self._following_id = id
