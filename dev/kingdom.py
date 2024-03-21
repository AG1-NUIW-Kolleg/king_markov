from __future__ import annotations

import os

import imageio
import matplotlib.pyplot as plt
import prettytable as pt

from constants import GENERATE_GIF
from constants import ITERATIONS
from constants import MAX_GIF_LEN
from constants import NUMBER_OF_ISLANDS
from constants import SAVE_DIR
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
        if (GENERATE_GIF is True and ITERATIONS > MAX_GIF_LEN):
            raise ValueError(
                'Travel loop cancelled. Too many frames.' +
                '\nChoose smaller number of iterations.',
            )
        else:
            fig, axs = plt.subplots(2, 1, layout='constrained')
            for island in self._islands:

                for ax in axs:
                    ax.grid(visible='true')
                    ax.set_axisbelow(True)
                    ax.set_xlabel('Island-ID')
                    ax.set_xticks(range(0, NUMBER_OF_ISLANDS))

                axs[0].set_ylabel('# visits', color='tab:blue')
                axs[0].bar(
                    x=island.get_id(), height=island.get_visit_count(),
                    color='tab:blue',
                )

                axs[1].set_ylabel('population size', color='tab:red')
                axs[1].bar(
                    x=island.get_id(),
                    height=island.get_population_size(), color='tab:red',
                )
                fig.suptitle(f'iteration: {int(iteration)}')
                plt.close(fig)

            if (GENERATE_GIF is True):
                if (os.path.exists(f'{SAVE_DIR}temp') is False):
                    os.makedirs(f'{SAVE_DIR}temp')
                fig.savefig(f'{SAVE_DIR}temp/{name}.png', bbox_inches='tight')
            else:
                fig.savefig(f'{SAVE_DIR}plots/{name}.png', bbox_inches='tight')

    def generate_gif(self, title: str):
        """Generates a GIF based on the saved frames in graphics/"""
        with imageio.get_writer(
            f'{SAVE_DIR}gifs/{title}.gif',
            mode='I',
            fps=5,
        ) as writer:
            for i in range(0, ITERATIONS):
                frame_filename = self._get_filename(iteration=i)
                image = imageio.imread(frame_filename)
                writer.append_data(image)

                if os.path.exists(frame_filename):
                    os.remove(frame_filename)

        if (self._is_temp_folder_empty()):
            os.rmdir(f'{SAVE_DIR}temp')
        else:
            raise FileNotFoundError(f'{SAVE_DIR}temp folder is not empty')

    def _is_temp_folder_empty(self) -> bool:
        """Returns whether the SAVE_DIR/temp folder is empty"""
        if (self._does_temp_folder_exist()):
            folder_list = os.listdir(f'{SAVE_DIR}temp')
            folder_len = len(folder_list)
            is_empty = False
            if (folder_len == 0):
                is_empty = True
            return is_empty
        else:
            raise FileNotFoundError(f'{SAVE_DIR}temp does not exist')

    def _does_temp_folder_exist(self) -> bool:
        """Returns whether the graphics/temp folder exists"""
        does_exist = False
        if (os.path.exists(f'{SAVE_DIR}temp')):
            does_exist = True
        return does_exist

    def _get_filename(self, iteration: int) -> str:
        """Returns the corresponding filename of a state"""
        save_filename = f'{SAVE_DIR}temp/state_{iteration}.png'
        return save_filename
