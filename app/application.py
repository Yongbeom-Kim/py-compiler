from compileall import compile_dir, compile_file
from pathlib import Path

import click


def compile_command(path: Path, recursive: bool, in_place: bool):
    click.echo(click.format_filename(path))

    path = Path(path)
    compileall(path, recursive)

    if (in_place):
        replace_py_with_pyc(path, recursive)


def compileall(path: Path, is_recursive: bool):
    """
    Simple wrapper around python compileall package to compile .py to .pyc files.

    Note that created .pyc files are under the __pycache__ directory.
    """
    assert (path.exists())

    if (path.is_dir()):
        max_recursion_levels = None if is_recursive else 0
        compile_dir(path, maxlevels=max_recursion_levels)
    elif (path.is_file()):
        assert (path.suffix == '.py')
        compile_file(path)


def replace_py_with_pyc(path: Path, is_recursive: bool):
    """Replace .py with .pyc files """
    assert (path.exists())

    if (path.is_dir()):
        _replace_py_with_pyc_dir(path, is_recursive)
    elif (path.is_file()):
        assert (path.suffix == '.py')
        _replace_py_with_pyc_file(path)


def _replace_py_with_pyc_dir(path: Path, is_recursive: bool):
    for child in path.iterdir():
        if (child.is_dir() and is_recursive):
            _replace_py_with_pyc_dir(child, is_recursive)
            continue

        if (child.is_file() and child.suffix == '.py'):
            _replace_py_with_pyc_file(child)
            continue


def _replace_py_with_pyc_file(python_file_path: Path):
    """Replace a .py file with its corresponding .pyc file in the __pycache__ directory."""
    assert (python_file_path.is_file() and python_file_path.suffix == '.py')
    compiled_file = _get_pycache_pyc_from_py(python_file_path)
    if (compiled_file is None):
        raise FileNotFoundError(
            f'.pyc file does not exist for the file {python_file_path.as_posix()}')
    python_file_path.unlink()
    compiled_file.rename(python_file_path.with_suffix('.pyc'))


def _get_pycache_pyc_from_py(python_file_path: Path) -> Path | None:
    """For a given .py file, get its corresponding .pyc file path in the __pycache__ directory."""
    assert (python_file_path.is_file() and python_file_path.suffix == '.py')
    pycache_dir = python_file_path.parent / '__pycache__'
    query = list(pycache_dir.glob(python_file_path.stem + '.cpython-*.pyc'))
    if (len(query) == 0):
        return None
    assert (len(query) == 1)
    compiled_file = query[0]

    return compiled_file
