from unittest import TestCase

from core.core import new_deck


class TestCore(TestCase):

    def test_new_deck(self):
        deck = new_deck()
        assert len(deck) == 52
