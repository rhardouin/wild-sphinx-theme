Wild Sphinx Theme
=================

Wild is a `Sphinx <http://sphinx.pocoo.org/>`_ theme based on Nature.
It allows you to use a `Pygments <http://pygments.org/>`_ style
with a dark background.

Installation
------------

1. Install the package::

    $ pip install wild-sphinx-theme

2. Edit your conf.py sphinx configuration file to use Wild theme::

    import wild_sphinx_theme
    html_theme = 'wild'
    html_theme_path = [wild_sphinx_theme.get_theme_dir()]

License
-------

Wild is released under the BSD License. 