#! /usr/bin/env python
import click
import pytest

from core.core import Core
from utils.configuration import Configuration

conf = Configuration()
conf.load_config()


@click.group()
def main():
    pass


@main.command()
@click.option('-p', '--players', type=int, help='Quantity of players, default value from interval placed in conf file',
              required=False)
@click.option('-d', '--debug', is_flag=True, default=False, required=False)
def run(players, debug):
    """Start a game"""
    if players is not None and conf.is_valid_quantity_players(players):
        players_quantity = players
    else:
        players_quantity = conf.get_random_players_quantity()
    core = Core()
    core.start(players_quantity, debug)


@main.command()
def learn():
    """Learn our bot using some type of learning"""
    print('learning')


@main.command()
def test():
    """Run unit test"""
    pytest.main(['-x', 'test'])


if __name__ == "__main__":
    main()
