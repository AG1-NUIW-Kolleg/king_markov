from __future__ import annotations

import prettytable as pt

from island import Island


class Kingdom:
    """Represents a kingdom holding a variable amount of islands"""

    def __init__(self, islands: list[Island]):
        self._islands: list[Island] = islands

    def get_island_by_id(self, id: int) -> Island:
        """Returns the island of the kingdom by its id"""
        try:
            island = self._islands[id]
        except IndexError as exc:
            raise IndexError(f'Island with id {id} does not exist') from exc

        return island

    def setup_island_order(self):
        """Sets up the islands in a circle"""
        last_island_id = len(self._islands) - 1

        i = 0
        for island in self._islands:
            island.set_id(id=i)
            island.set_following_id(id=i+1)
            island.set_preceding_id(id=i-1)
            i += 1

        # close circle
        self._islands[last_island_id].set_following_id(id=0)
        self._islands[0].set_preceding_id(id=last_island_id)

    def print(self):
        """Prints the kingdom as a table"""
        table = pt.PrettyTable(
            field_names=[
                'island-ID', 'preceding-ID',
                'following-ID', 'population size', 'king visit count',
            ],
        )
        table.align['population size'] = 'r'
        table.align['king visit count'] = 'r'

        for island in self._islands:
            table.add_row(
                [
                    island.get_id(), island.get_preceding_id(),
                    island.get_following_id(), island.get_population_size(),
                    island.get_visit_count(),
                ],
            )

        print(table)
