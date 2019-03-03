import random

import yaml


class Configuration(object):

    def __init__(self):
        [self._config, self._run_config, self._min_players, self._max_players] = [None for _ in range(4)]

    def get_random_players_quantity(self) -> int:
        options = range(self._min_players, self._max_players + 1)
        return random.sample(options, 1)[0]

    def is_valid_quantity_players(self, players) -> bool:
        result = self._max_players >= int(players) >= self._min_players
        print("Number of players is wrong, It will be random")
        return result

    def load_config(self):
        with open('utils/configuration.yaml') as configuration_file:
            self._config = yaml.load(configuration_file.read())

        self._run_config = self._config['run']
        self._min_players = self._run_config['min_players']
        self._max_players = self._run_config['max_players']

        self._min_players = 2 if self._min_players < 2 else self._min_players
        if self._max_players <= self._min_players:
            raise ValueError("Wrong number of players")
