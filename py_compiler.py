from pathlib import Path
import click
from app.application import compile_command, compileall, replace_py_with_pyc


@click.group()
def cli():
    pass


@cli.command()
@click.option('-recursive', '-r', is_flag=True, default=True, help='Recurse through subdirectories.')
@click.option('--in-place', is_flag=True, default=False, help='Remove .py and replace them with compiled .pyc files.')
@click.argument('path', type=click.Path(exists=True))
def compile(recursive, in_place, path):
    compile_command(path, recursive=recursive, in_place=in_place)
