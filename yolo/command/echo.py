import click
import logging

logger = logging.getLogger(__name__)

@click.command(
    name="echo",
    short_help="Echo a response to the user",
)
@click.option(
    "--message",
    "-m",
    type=str,
    required=True,
    help="The message to echo to the user"
)
def echo(message: str):
    print(message)
