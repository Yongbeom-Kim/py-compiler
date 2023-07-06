from pathlib import Path
import click
from app.application import compile_command


@click.group()
def cli():
    pass


@cli.command()
@click.option('-recursive', '-r', is_flag=True, default=False, help='Recurse through subdirectories.')
@click.option('--in-place', is_flag=True, default=False, help='Remove .py and replace them with compiled .pyc files.')
@click.option('--create-empty-init', is_flag=True, default=False, help='Create an empty __init__.py file in the base directory path specified after compilation. Useful for interacting with tools such as colcon.')
@click.option('--exclude', '-e', multiple=True, help='Exclude pattern(s) for files to be excluded during compilation and replacement.')
@click.argument('paths', type=click.Path(exists=True), nargs=-1)
def compile(paths, recursive, in_place, create_empty_init, exclude):
    for path in paths:
        compile_command(
            Path(path),
            recursive=recursive,
            in_place=in_place,
            create_empty_init=create_empty_init,
            exclude_patterns=exclude
        )
