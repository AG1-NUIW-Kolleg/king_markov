from __future__ import annotations

import matplotlib.pyplot as plt
import prettytable as pt

from dev.island import Island


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

    def plot_visits(self, name: str, iteration: int):
        """Plots the visit counts of a kingdom in a histogram"""
        fig, axs = plt.subplots(2, 1, layout='constrained')
        for island in self._islands:

            for ax in axs:
                ax.grid(visible='true')
                ax.set_axisbelow(True)
                ax.set_xticks(range(0, 5), [1, 2, 3, 4, 5])

            axs[0].set_xlabel('Working Group')
            axs[0].set_ylabel('number of visits', color='tab:blue')

            axs[0].bar(
                x=island.get_id(), height=island.get_visit_count(),
                color='tab:blue',
            )

            axs[1].set_xlabel('Working Group')
            axs[1].set_ylabel('# publications', color='tab:red')
            axs[1].bar(
                x=island.get_id(),
                height=island.get_population_size(), color='tab:red',
            )
            fig.suptitle(f'days spent: {iteration+1}')

        fig.savefig(f'graphics/{name}.png')
