wild-sphinx-theme
=================

Wild is a Sphinx theme based on Nature. It allows you to use a pygments style with a dark background.

Installation
------------

Declare you want to use wild theme in conf.py:

    html_theme = 'wild'

Ensure to properly set theme directory too.  
Assuming your theme directory is `<sphinx dir>/_theme` your conf.py should contain:

    html_theme_path = ['_themes']
    
Directory tree example
------------------------

    + <sphinx directory>
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
                