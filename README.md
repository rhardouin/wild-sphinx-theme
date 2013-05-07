wild-sphinx-theme
=================

Wild is a Sphinx theme based on Nature. It allows you to use a pygments style with a dark background.

Manual installation
===================

Declare you want to use wild theme in conf.py:

    html_theme = 'wild'

Ensure to properly set theme directory too.  
Assuming your theme directory is `<sphinx dir>/_theme` your conf.py should contain:

    html_theme_path = ['_themes']
    
Directory tree example
----------------------

    + <sphinx directory>
        |
        - conf.py
        |
        - index.rst
        |
        + ...
        |
        + _themes
            |
            + wild
                |
                - theme.conf
                |
                + static
                    |
                    - wild.css_t

PIP Installation
================

Coming soon.