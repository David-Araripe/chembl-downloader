# -*- coding: utf-8 -*-

"""CLI for :mod:`chembl_downloader`."""
from typing import Optional

import click
from more_click import verbose_option
from tabulate import tabulate

from .api import get_cursor

__all__ = [
    'main',
]

QUERY = """
SELECT
    MOLECULE_DICTIONARY.chembl_id,
    MOLECULE_DICTIONARY.pref_name
FROM MOLECULE_DICTIONARY
JOIN COMPOUND_STRUCTURES ON MOLECULE_DICTIONARY.molregno == COMPOUND_STRUCTURES.molregno
WHERE molecule_dictionary.pref_name IS NOT NULL
LIMIT 5
"""


@click.command()
@verbose_option
@click.option('--version')
def main(version: Optional[str]):
    """Test the connection."""
    with get_cursor(version=version) as cursor:
        click.echo(f"using cursor {cursor}")
        cursor.execute(QUERY)
        click.echo(tabulate(
            cursor.fetchall(),
            headers=['chembl_id', 'name'],
        ))


if __name__ == '__main__':
    main()
