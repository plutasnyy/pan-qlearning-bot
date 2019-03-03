from unittest import TestCase
from utils.configuration import Configuration


class TestConfiguration(TestCase):

    def test_get_random_players_quantity(self):
        conf = Configuration()
        conf._min_players = 2
        conf._max_players = 6
        result = conf.get_random_players_quantity()
        assert result >= 2
        assert result <= 6

    def test_is_valid_quantity_players(self):
        conf = Configuration()
        conf._min_players = 2
        conf._max_players = 6

        assert conf.is_valid_quantity_players(2) is True
        assert conf.is_valid_quantity_players(3) is True
        assert conf.is_valid_quantity_players(6) is True
        assert conf.is_valid_quantity_players(1) is False
        assert conf.is_valid_quantity_players(7) is False

