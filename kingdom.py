from __future__ import annotations

from island import Island


class Kingdom:
    """Represents a kingdom holding a variable amount of islands"""

    def __init__(self, islands: list[Island]):
        self._islands: list[Island] = islands
