import os

__version__ = '1.0.1'


def get_theme_dir():
    return os.path.abspath(os.path.dirname(__file__))
