from pathlib import Path

path = Path(__file__).resolve().parent

PATH = path / 'dummy.txt'

def func_path():
    return PATH