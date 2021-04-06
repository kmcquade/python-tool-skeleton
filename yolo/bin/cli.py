#! /usr/bin/env python
import click
from yolo.command.echo import echo
from yolo.bin.version import __version__


@click.group()
@click.version_option(version=__version__)
def yolo():
    """
    An example tool.
    """


yolo.add_command(echo)


def main():
    """An example tool"""
    yolo()


if __name__ == '__main__':
    main()
