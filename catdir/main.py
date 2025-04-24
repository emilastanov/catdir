from typing import Iterable
import click
import os

from catdir.constants import NOISE
from catdir.dump import dump


def handler(path: str, exclude: Iterable[str], exclude_noise: bool) -> None:
    absolute_path = os.path.abspath(path)

    # Use a set for efficient lookups and to avoid duplicates
    exclude_content = set(exclude)
    if exclude_noise:
        exclude_content.update(NOISE)

    content = dump(absolute_path, exclude_content)
    click.echo(content)


@click.command(
    context_settings=dict(help_option_names=["--help", "-h"]),
    help="""
CATDIR — Concatenate contents of all files in a directory, like `cat`, but for entire folders.

Example:
    catdir ./my_project --exclude .env --exclude-noise

This will output the combined contents of all files, excluding `.env` and standard noise like `.git`, `node_modules`, etc.
"""
)
@click.option(
    "-e", "--exclude",
    multiple=True,
    help="""
Manually exclude specific files or folders.

You can use this option multiple times:
    --exclude .env --exclude secrets.json
"""
)
@click.option(
    "-en", "--exclude-noise",
    is_flag=True,
    help="""
Exclude common development noise:
temporary, cache, build, and system files that are usually not needed in a dump.

Includes: .git, .venv, __pycache__, node_modules, and more.
"""
)
@click.argument("path")
def catdir(path: str, exclude: Iterable[str], exclude_noise: bool) -> None:
    """
    Concatenate and print the contents of all files in the given folder.

    Args:
        path (str): Relative or absolute path to the directory.
        exclude (Iterable[str]): Items to exclude by name (file or folder names).
        exclude_noise (bool): Whether to include standard development artifacts in the exclusion list.
    """
    handler(path, exclude, exclude_noise)
