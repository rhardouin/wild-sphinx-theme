#!/bin/python33

from distutils.core import setup
import wild_sphinx_theme

with open('README.txt', 'r') as f:
    desc = f.read()

setup(name='wild_sphinx_theme',
    version=__import__('wild_sphinx_theme').__version__,
    description='Like Nature sphinx theme but allows pygments style to be dark',
    long_description=desc,
    packages=['wild_sphinx_theme'],
    package_data={"wild_sphinx_theme": ["wild/*.*", "wild/static/*.*"]},
    url='https://github.com/rhardouin/wild-sphinx-theme',
    author='Romain Hardouin',
    author_email='romain_hardouin@yahoo.fr',
    license = "BSD",
    keywords = "sphinx extension theme",
    #download_url = "TBD",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ]
)